import json
import traceback
from sqlalchemy import select, and_, update
from common.database import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from module.bucket.borrowing_bucket.schemas.borrowing_bucket_schemas import BorrowingBucketCreate
from module.bucket.borrowing_bucket.services.borrowing_bucket_services import BorrowingBucketService
from module.bucket.customer_actual_holdings.schemas.customer_actual_holdings_schemas import ActualHoldingsUpdate
from module.bucket.customer_actual_holdings.services.customer_actual_holdings_service import \
    CustomerActualHoldingsBucketService
from module.car.modules.car_module import Car
from module.goods.modules.car_goods_module import CarGoods
from module.goods.modules.goods_module import Goods
from module.goods.modules.inventory_total_module import GoodsTotal
from module.goods.modules.record_module import CarGoodsRecord, StoreGoodsRecord
from module.order.schemas.order_schemas import OrderSchemas
from module.water_ticket.ele_water_ticket.cruds.ele_water_ticket_crud import EleWaterTicketCRUD
from module.water_ticket.ele_water_ticket.modules.ele_water_ticket_module import EleWaterTicket
from module.water_ticket.ele_water_ticket.schemas.ele_water_ticket_schema import BuyTicket
from module.water_ticket.ele_water_ticket.services.ele_water_ticket_service import EleWaterTicketService
from module.water_ticket.water_ticket_package.modules.water_ticket_package_module import WaterPackage


class ProcessOrderAction:
    def __init__(self, db: AsyncSession, order_info: OrderSchemas, before_state=None):
        """
        order_info 订单信息
        before_state 订单前置状态
        """
        self.db = db
        self.order_info = order_info
        self.before_state = int(before_state) if before_state else None
        self.current_state = int(self.order_info.state) if self.order_info.state else None
        self.action_state_tuple = tuple((self.before_state, self.current_state))

    async def process_state(self):
        """
        1、待支付，2、待派单，3、待配送，4、配送中，5、已取消，6、已完成、7、退货中、8、换货中，9、已退款

        -----商品
            **state1
            待支付
            none --> 1 (none --> 待支付)
                1.商品库存扣减 	2.电子水票扣减
                (可以取消订单)

            **state2
            待派单（代客下单）
            none --> 2 (none --> 待派单)
                1.商品库存扣减 	2.电子水票扣减
                (可以退款)
            1-->2  (待支付 --> 待派单)
                (可以退款)

            **state3
            待配送
            2-->3 (待派单 --> 待配送)
                （**不能退款）

            **state4
            配送中
            3-->4 (待配送 --> 配送中)
                （**不能退款）

            **state5
            已取消
            1-->5 (待支付 --> 已取消)
                1.商品补回库存

            **state6
            已完成
            4-->6 (配送中 --> 已完成)
                1.根据订单商品计算借/回桶
                （可以退款 使用水票的不能退款）

            **state7
            退货中
            6-->7 (已完成 --> 退货中)
                none
            2-->7 (待配送 --> 退货中)
                none

            **state8
            换货中
            6-->8 (已完成 --> 换货中)
                none

            **state9
            已退款
            7-->9 (退货中 --> 已退款)
                1.商品库存补回  2.桶数据（区分已完成的退款还是已完成状态前的退款 已完成前-不改桶数据  已完成后的退款--客户实际持桶 0）


        -----水票套餐
            **state1
            待支付
            none --> 1 (none --> 待支付)
                1.可以取消订单

            **state6
            已完成
            1-->6 (待支付 --> 已完成)
                1.根据订单套餐分配水票
                (不能退款)
            none --> 6 （代客下单）(none --> 已完成)
                1.根据订单套餐分配水票
        """
        # 1、待支付，2、待派单，3、待配送，4、配送中，5、已取消，6、已完成、7、退货中、8、换货中，9、已退款
        state_actions = {
            (None, 1): self.pending_goods_water_ticket_sub,     # 待支付：商品库存扣减（总库存） 电子水票扣减
            (None, 2): self.pending_goods_water_ticket_sub,  # 待派单（代客下单）：商品库存扣减（总库存） 电子水票扣减
            (3, 4): self.car_or_store_stock_sub,    #   扣除具体库存（查询配送员是属于配送车还是门店 扣除对应库存）
            (4, 6): self.complete_borrowing_compute,     # 已完成：根据订单商品计算借/回桶
            (1, 6): self.water_ticket_allocate,      # 已完成：根据订单套餐分配水票
            (None, 6): self.water_ticket_allocate,  # 已完成（代客下单）：根据订单套餐分配水票
            (1, 5): self.cancel_make_up_goods_water_ticket,  # 已取消：商品补回库存
            # 已退款 商品补回库存 桶数据 使用水票的不能退款（区分已完成的退款还是已完成状态前的退款 *已完成前-不改桶数据  *已完成后的退款--客户实际持桶改0）
            # 退货中退款
            (7, 9): self.refund_make_up_goods_bucket,
            # 已完成退款
            (6, 9): self.refund_make_up_goods_bucket,
            # 待派单退款
            (2, 9): self.refund_make_up_goods_bucket,
        }
        action = state_actions.get(self.action_state_tuple)
        if action:
            return await action()
        else:
            return True

    async def car_or_store_stock_sub(self):
        """
        扣除具体库存（查询配送员是属于配送车还是门店 扣除对应库存）
        """
        if not self.order_info.water_delivery_worker:
            raise Exception(f"没有配送员信息")

        employee_id = self.order_info.water_delivery_worker.id

        car = select(Car.id).where(Car.driver == employee_id)
        car_result = await self.db.execute(car)
        car_id = car_result.scalar_one_or_none()

        # 提取商品 ID 和数量映射
        goods_id_to_num = {item.goods_id: item.quantity for item in self.order_info.order_goods_list}
        goods_ids = list(goods_id_to_num.keys())

        if car_id:
            # 扣除送水车库存
            # 1.查询商品信息
            stmt_stock = select(CarGoods).where(CarGoods.car_id == car_id, CarGoods.goods_id.in_(goods_ids))

            result_stock = await self.db.execute(stmt_stock)
            goods_stock_list = result_stock.scalars().all()

            # 2. 将查询结果构建成 id -> 商品对象的映射
            goods_stock_map = {goods_stock.goods_id: goods_stock for goods_stock in goods_stock_list}

            # 3. 内存中校验：存在性、状态、库存是否充足
            for goods_obj in self.order_info.order_goods_list:
                _goods_info = json.loads(goods_obj.good_info)

                goods_id = goods_obj.goods_id
                num = goods_obj.quantity

                goods_stock = goods_stock_map.get(goods_id)
                if not goods_stock:
                    raise Exception(f"车辆: {car_id} 商品 {goods_id} 不存在或已下架")

                if goods_stock.stock < num:
                    raise Exception(
                        f"车辆: {car_id} 商品 {goods_stock.name} 库存不足，当前库存: {goods_stock.stock}，需扣减: {num}")

                new_stock = goods_stock.stock - num
                # 记录
                self.db.add(
                    CarGoodsRecord(
                        car_id=car_id,
                        order_id=self.order_info.id,
                        store_id=_goods_info.get("store_id"),
                        goods_id=goods_id,
                        stock_initial=goods_stock.stock,
                        action="配送扣库存",
                        action_id=1,
                        stock_change=num,
                        stock_completion=new_stock,
                        operator=self.order_info.water_delivery_worker.user.user_info.name,
                        operator_id=self.order_info.water_delivery_worker.id
                    )
                )

                # 预扣库存（暂不持久化）
                goods_stock.stock = new_stock

            await self.db.commit()

            # 5. 触发库存预警（可选异步处理）
            # for goods in goods_stock_list:
            #     if goods.stock < 20:
            #         # 库存低于预警值
            #         pass
        else:
            # 扣店铺库存
            # 1.查询商品信息
            stmt_stock = select(Goods).where(Goods.id.in_(goods_ids))

            result_stock = await self.db.execute(stmt_stock)
            goods_stock_list = result_stock.scalars().all()

            # 2. 将查询结果构建成 id -> 商品对象的映射
            goods_stock_map = {goods_stock.id: goods_stock for goods_stock in goods_stock_list}

            # 3. 内存中校验：存在性、状态、库存是否充足
            for goods_obj in self.order_info.order_goods_list:
                _goods_info = json.loads(goods_obj.good_info)

                goods_id = goods_obj.goods_id
                num = goods_obj.quantity

                goods_stock = goods_stock_map.get(goods_id)
                if not goods_stock:
                    raise Exception(f"门店商品 {goods_id} 不存在或已下架")

                if goods_stock.stock < num:
                    raise Exception(f"门店商品 {goods_stock.name} 库存不足，当前库存: {goods_stock.stock}，需扣减: {num}")

                new_stock = goods_stock.stock - num
                self.db.add(
                    StoreGoodsRecord(
                        order_id=self.order_info.id,
                        store_id=_goods_info.get("store_id"),
                        goods_id=goods_id,
                        stock_initial=goods_stock.stock,
                        action="配送扣库存",
                        action_id=1,
                        stock_change=num,
                        stock_completion=new_stock,
                        operator=self.order_info.water_delivery_worker.user.user_info.name,
                        operator_id=self.order_info.water_delivery_worker.id
                    )
                )

                # 预扣库存（暂不持久化）
                goods_stock.stock = new_stock

            await self.db.commit()

            # 5. 触发库存预警（可选异步处理）
            # for goods in goods_stock_list:
            #     if goods.stock < 20:
            #         # 库存低于预警值
            #         pass

        return True

    async def pending_goods_water_ticket_sub(self):
        """
        商品库存扣减 电子水票扣减
        """
        try:
            """
            self.order_info.order_goods_list   self.order_info.order_water_tickets 要保证两个数据不同时存在
            """
            # 1.商品库存扣减
            if self.order_info.order_goods_list:
                await self.decrease_stock()

            # 2.电子水票扣减
            #  水票单 order_goods_list 为空列表
            if self.order_info.order_water_tickets:
                """
                ticket_info：
                主键id, 数量, 水票类型（1电子水票 2纸质水票）,票码
                电子
                {"id": 1, "num": 11, "type": 1}
                纸质  纸质数量都为 1
                {"id": 2, "num": 1, "type": 2, "code": 213}
                """
                # 水票
                await self.ele_water_ticket_sub()
                # 商品
                await self.water_goods_decrease_stock()

            return True

        except Exception as e:
            await self.db.rollback()
            traceback.print_exc()
            if isinstance(e.args, tuple) and isinstance(e.args[0], dict) and e.args[0].get("detail"):
                raise Exception(e.args[0].get("detail"))

            raise Exception(f"库存扣减时发生错误请联系管理员")

    async def complete_borrowing_compute(self):
        """
        根据订单商品计算借/回桶
        """
        try:
            # 回桶
            return_bucket_dict = {}
            if self.order_info.order_return_bucket:
                for goods_obj in self.order_info.order_return_bucket:
                    bucket_id = goods_obj.bucket_id
                    num = goods_obj.quantity
                    return_bucket_dict[bucket_id] = num

            # 商品桶
            ues_bucket_dict = {}
            if self.order_info.order_goods_list:
                for goods_obj in self.order_info.order_goods_list:
                    binding_bucket_id = goods_obj.goods.get("binding_bucket_id")
                    if binding_bucket_id:
                        num = goods_obj.quantity
                        ues_bucket_dict[binding_bucket_id] = num

            add_dict = {}
            sub_dict = {}
            # 遍历商品桶
            # 回桶数量少于商品桶是增加借桶
            # 回桶数量大于于商品桶是减少借桶
            for goods_bucket_id, num in ues_bucket_dict.items():
                return_bucket_num = return_bucket_dict.get(goods_bucket_id)
                if return_bucket_num:
                    difference = num - return_bucket_num
                    if difference == 0:
                        continue
                    if difference > 0:
                        # 回桶少于商品桶是借桶
                        add_dict[goods_bucket_id] = difference
                    else:
                        sub_dict[goods_bucket_id] = return_bucket_num - num
                else:
                    # 没有回桶就是借桶
                    add_dict[goods_bucket_id] = num

            # 遍历回桶数据
            # 回桶数量少于商品桶是增加借桶
            # 回桶数量大于于商品桶是减少借桶
            for return_bucket_id, num in return_bucket_dict.items():
                if not ues_bucket_dict.get(return_bucket_id):
                    # 如果回桶数据不存在商品数据里  那么直接算回桶数据
                    sub_dict[return_bucket_id] = num
                # 如果在商品数据里 上面已经处理过

            borrowing_bucket_service = BorrowingBucketService(self.db)
            if add_dict:
                # 借桶
                await borrowing_bucket_service.add_borrow_bucket(
                    BorrowingBucketCreate(
                        store_id=self.order_info.store_id,
                        customer_id=self.order_info.customer_id,
                        bucket_detail=[{"id": key, "num": value} for key, value in add_dict.items()],
                    )
                )
            if sub_dict:
                # 回桶
                await borrowing_bucket_service.return_bucket(
                    BorrowingBucketCreate(
                        store_id=self.order_info.store_id,
                        customer_id=self.order_info.customer_id,
                        bucket_detail=[{"id": key, "num": value} for key, value in sub_dict.items()],
                    )
                )

            return True

        except Exception as e:
            await self.db.rollback()
            traceback.print_exc()
            if isinstance(e.args, tuple) and isinstance(e.args[0], dict) and e.args[0].get("detail"):
                raise Exception(e.args[0].get("detail"))

            raise Exception(f"借/回桶计算错误-001")

    async def cancel_make_up_goods_water_ticket(self):
        """
        已取消
        1.商品补回库存
        """
        try:
            # 1.商品补回库存
            if self.order_info.order_goods_list:
                await self.replenished_stock()

            return True

        except Exception as e:
            await self.db.rollback()
            traceback.print_exc()
            if isinstance(e.args, tuple) and isinstance(e.args[0], dict) and e.args[0].get("detail"):
                raise Exception(e.args[0].get("detail"))
            raise Exception(f"取消订单发生错误-001")

    async def refund_make_up_goods_bucket(self):
        """
        已退款
        1.商品补回库存
        2.桶数据（区分已完成的退款还是已完成状态前的退款 *已完成前-不改桶数据  *已完成后的退款--客户实际持桶改0）
        使用水票的不能退款
        """
        # 使用水票的不能退款
        if self.order_info.order_water_tickets:
            raise Exception(f"使用水票的订单不能退款")

        # 1.商品补回库存
        if self.order_info.order_goods_list:
            await self.replenished_stock()

        # 2.桶数据 （仅针对于退款全退的情况）
        if self.order_info.is_ok:
            # 客户实际持桶改0 借桶改0
            await CustomerActualHoldingsBucketService(self.db).update_actual_holdings_bucket(
                ActualHoldingsUpdate(
                    store_id=self.order_info.store_id,
                    customer_id=self.order_info.customer_id,
                    bucket_detail=[]
                )
            )

    async def replenished_stock(self):
        """
        商品补回库存
        """
        try:
            if not self.order_info.order_goods_list:
                return True

            # 提取商品 ID 和数量映射
            goods_id_to_num = {item.goods_id: item.quantity for item in self.order_info.order_goods_list}
            goods_ids = list(goods_id_to_num.keys())

            # 1. 查询商品信息
            stmt_stock = select(GoodsTotal).where(GoodsTotal.goods_id.in_(goods_ids))

            result_stock = await self.db.execute(stmt_stock)
            goods_stock_list = result_stock.scalars().all()

            # 2. 将查询结果构建成 id -> 商品对象的映射
            goods_stock_map = {goods_stock.goods_id: goods_stock for goods_stock in goods_stock_list}

            # 3. 内存中校验：存在性
            for goods_obj in self.order_info.order_goods_list:
                goods_id = goods_obj.goods_id
                num = goods_obj.quantity

                goods_stock = goods_stock_map.get(goods_id)
                if not goods_stock:
                    continue
                    # raise Exception({
                    #     "detail": f"商品 {goods_id} 不存在"
                    # })

                # 补回库存（暂不持久化）
                goods_stock.stock += num


            # 已完成的退款退款需要计算具体哪个源的库存（店铺/车）
            if self.order_info.is_ok:
                stmt_record = select(CarGoodsRecord).where(CarGoodsRecord.order_id == self.order_info.id,
                                                           CarGoodsRecord.action_id == 1)
                result_stock = await self.db.execute(stmt_record)
                goods_record_list = result_stock.scalars().all()

                car_id = None
                # 车库存变动记录
                if goods_record_list:
                    car = select(Car.id).where(Car.driver == self.order_info.water_delivery_worker.id)
                    car_result = await self.db.execute(car)
                    car_id = car_result.scalar_one_or_none()

                if car_id:
                    for goods_record_obj in goods_record_list:
                        car_goods_result = await self.db.execute(
                            select(CarGoods)
                            .where(CarGoods.car_id==car_id, CarGoods.goods_id==goods_record_obj.goods_id)
                        )
                        car_goods_obj = car_goods_result.scalar_one_or_none()
                        # 车库存处理
                        if car_goods_obj:
                            new_stock = car_goods_obj.stock + goods_record_obj.stock_change
                            # 记录
                            self.db.add(
                                CarGoodsRecord(
                                    car_id=car_id,
                                    order_id=self.order_info.id,
                                    store_id=car_goods_obj.store_id,
                                    goods_id=car_goods_obj.goods_id,
                                    stock_initial=car_goods_obj.stock,
                                    action="退货",
                                    action_id=2,
                                    stock_change=goods_record_obj.stock_change,
                                    stock_completion=new_stock,
                                    operator=self.order_info.water_delivery_worker.user.user_info.name,
                                    operator_id=self.order_info.water_delivery_worker.id
                                )
                            )
                            car_goods_obj.stock = new_stock
                        else:
                            self.db.add(
                                CarGoods(
                                    store_id=goods_record_obj.store_id,
                                    car_id=car_id,
                                    goods_id=car_goods_obj.goods_id,
                                    stock=goods_record_obj.stock_change
                                )
                            )
                            # 记录
                            self.db.add(
                                CarGoodsRecord(
                                    car_id=car_id,
                                    order_id=self.order_info.id,
                                    store_id=car_goods_obj.store_id,
                                    goods_id=car_goods_obj.goods_id,
                                    stock_initial=car_goods_obj.stock,
                                    action="退货",
                                    action_id=2,
                                    stock_change=goods_record_obj.stock_change,
                                    stock_completion=goods_record_obj.stock_change,
                                    operator=self.order_info.water_delivery_worker.user.user_info.name,
                                    operator_id=self.order_info.water_delivery_worker.id
                                )
                            )

                        # 总库存
                        update_stmt = (
                            update(GoodsTotal)
                            .where(GoodsTotal.store_id == car_goods_obj.store_id, GoodsTotal.goods_id == car_goods_obj.goods_id)
                            .values(stock=GoodsTotal.stock+goods_record_obj.stock_change)
                        )
                        await self.db.execute(update_stmt)
                else:
                    # 店铺库存变动记录
                    stmt_record = select(StoreGoodsRecord).where(StoreGoodsRecord.order_id == self.order_info.id,
                                                               StoreGoodsRecord.action_id == 1)
                    result_stock = await self.db.execute(stmt_record)
                    goods_record_list = result_stock.scalars().all()

                    for goods_record_obj in goods_record_list:
                        store_goods_result = await self.db.execute(select(Goods).where(Goods.id==goods_record_obj.goods_id))
                        store_goods_obj = store_goods_result.scalar_one_or_none()

                        new_stock = store_goods_obj.stock + goods_record_obj.stock_change
                        # 记录
                        self.db.add(
                            StoreGoodsRecord(
                                order_id=self.order_info.id,
                                store_id=goods_record_obj.store_id,
                                goods_id=goods_record_obj.goods_id,
                                stock_initial=store_goods_obj.stock,
                                action="退货",
                                action_id=2,
                                stock_change=goods_record_obj.stock_change,
                                stock_completion=new_stock,
                                operator=self.order_info.water_delivery_worker.user.user_info.name,
                                operator_id=self.order_info.water_delivery_worker.id
                            )
                        )
                        store_goods_obj.stock = new_stock

                        # 总库存
                        update_stmt = (
                            update(GoodsTotal)
                            .where(GoodsTotal.store_id == goods_record_obj.store_id, GoodsTotal.goods_id == goods_record_obj.goods_id)
                            .values(stock=GoodsTotal.stock + goods_record_obj.stock_change)
                        )
                        await self.db.execute(update_stmt)

            await self.db.commit()

            return True

        except Exception as e:
            traceback.print_exc()
            await self.db.rollback()
            if isinstance(e.args, tuple) and isinstance(e.args[0], dict) and e.args[0].get("detail"):
                raise Exception(e.args[0].get("detail"))
            raise Exception("取消订单发生错误-002")   # 商品补回库存时发生错误


    async def decrease_stock(self):
        """
        商品扣库存：使用批量查询和更新，减少数据库交互次数
        """
        try:
            if not self.order_info.order_goods_list:
                return True

            # 提取商品 ID 和数量映射
            goods_id_to_num = {item.goods_id: item.quantity for item in self.order_info.order_goods_list}
            goods_ids = list(goods_id_to_num.keys())

            # 1.查询商品信息
            stmt_stock = select(GoodsTotal).where(GoodsTotal.goods_id.in_(goods_ids))

            result_stock = await self.db.execute(stmt_stock)
            goods_stock_list = result_stock.scalars().all()

            stmt_info = select(Goods).where(
                and_(
                    Goods.id.in_(goods_ids),
                    Goods.is_deleted == False,
                    Goods.status == True
                )
            )

            result_info = await self.db.execute(stmt_info)
            goods_info_list = result_info.scalars().all()

            # 2. 将查询结果构建成 id -> 商品对象的映射
            goods_stock_map = {goods_stock.goods_id: goods_stock for goods_stock in goods_stock_list}
            goods_info_map = {goods_info.id: goods_info for goods_info in goods_info_list}

            # 3. 内存中校验：存在性、状态、库存是否充足
            for goods_obj in self.order_info.order_goods_list:
                goods_id = goods_obj.goods_id
                num = goods_obj.quantity

                goods_stock = goods_stock_map.get(goods_id)
                goods_info = goods_info_map.get(goods_id)
                if not goods_stock or not goods_info:
                    raise Exception({
                        "detail": f"商品【{goods_info.name}】已下架"
                    })

                if goods_stock.stock < num:
                    # raise Exception({
                    #     "detail": f"商品 {goods_info.name} 库存不足，当前库存: {goods_stock.stock}，需扣减: {num}"
                    # })
                    raise Exception({
                        "detail": f"商品【{goods_info.name}】库存不足"
                    })

                # 预扣库存（暂不持久化）
                goods_stock.stock -= num

            await self.db.commit()

            # 增加销量
            for goods_obj in self.order_info.order_goods_list:
                goods_id = goods_obj.goods_id
                num = goods_obj.quantity

                goods_info = goods_info_map.get(goods_id)
                goods_info.sales += num
                goods_info.virtual_sales += num

            await self.db.commit()

            # 5. 触发库存预警（可选异步处理）
            for goods in goods_stock_list:
                if goods.stock < (goods_info_map.get(goods.goods_id).warning_value or 20):
                    # TODO 库存低于预警值
                    pass
                if goods.stock == 0:
                    # 没有库存下架商品
                    goods.status = False

            return True

        except Exception as e:
            traceback.print_exc()
            await self.db.rollback()
            if isinstance(e.args, tuple) and isinstance(e.args[0], dict) and e.args[0].get("detail"):
                raise Exception({
                    "detail": e.args[0].get("detail"),
                    "exception": e
                })
            raise Exception({
                "detail": f"商品扣库存时发生错误-001",
                "exception": e
            })

    async def water_goods_decrease_stock(self):
        """
        水票的商品扣库存
        """
        try:
            # self.order_info.order_water_tickets
            # 提取商品 ID 和数量映射
            goods_id_to_num = {item.goods.id: item.quantity for item in self.order_info.order_water_tickets}
            goods_ids = list(goods_id_to_num.keys())

            # 1.查询商品信息
            stmt_stock = select(GoodsTotal).where(GoodsTotal.goods_id.in_(goods_ids))

            result_stock = await self.db.execute(stmt_stock)
            goods_stock_list = result_stock.scalars().all()

            stmt_info = select(Goods).where(
                and_(
                    Goods.id.in_(goods_ids),
                    Goods.is_deleted == False,
                    Goods.status == True
                )
            )

            result_info = await self.db.execute(stmt_info)
            goods_info_list = result_info.scalars().all()

            # 2. 将查询结果构建成 id -> 商品对象的映射
            goods_stock_map = {goods_stock.goods_id: goods_stock for goods_stock in goods_stock_list}
            goods_info_map = {goods_info.id: goods_info for goods_info in goods_info_list}

            # 3. 内存中校验：存在性、状态、库存是否充足
            for goods_obj in self.order_info.order_water_tickets:
                goods_id = goods_obj.goods.id
                num = goods_obj.quantity

                goods_stock = goods_stock_map.get(goods_id)
                goods_info = goods_info_map.get(goods_id)
                if not goods_stock or not goods_info:
                    raise Exception({
                        "detail": f"商品【{goods_info.name}】已下架"
                    })

                if goods_stock.stock < num:
                    # raise Exception({
                    #     "detail": f"商品 {goods_info.name} 库存不足，当前库存: {goods_stock.stock}，需扣减: {num}"
                    # })
                    raise Exception({
                        "detail": f"商品【{goods_info.name}】库存不足"
                    })

                # 预扣库存（暂不持久化）
                goods_stock.stock -= num

            await self.db.commit()

            # 增加销量
            for goods_obj in self.order_info.order_water_tickets:
                goods_id = goods_obj.goods.id
                num = goods_obj.quantity

                goods_info = goods_info_map.get(goods_id)
                goods_info.sales += num
                goods_info.virtual_sales += num

            await self.db.commit()

            # 5. 触发库存预警（可选异步处理）
            for goods in goods_stock_list:
                if goods.stock < (goods_info_map.get(goods.goods_id).warning_value or 20):
                    # TODO 库存低于预警值
                    pass
                if goods.stock == 0:
                    # 没有库存下架商品
                    goods.status = False

            return True

        except Exception as e:
            traceback.print_exc()
            await self.db.rollback()
            if isinstance(e.args, tuple) and isinstance(e.args[0], dict) and e.args[0].get("detail"):
                raise Exception({
                    "detail": e.args[0].get("detail"),
                    "exception": e
                })
            raise Exception({
                "detail": f"商品扣库存时发生错误-011",
                "exception": e
            })

    async def ele_water_ticket_sub(self):
        """
        电子水票扣除
        {"id“: 1, "num": 11, "type": 1}
        """
        try:
            ticket_info = [{
                "water_ticket_id": i.water_ticket_id,
                "water_ticket_primary_key_id":  i.water_ticket_primary_key_id,
                "num": i.quantity,
                "type": 1
            } for i in self.order_info.order_water_tickets]

            if not ticket_info:
                # 没有电子水票
                return True

            # 扣除电子水票
            if ticket_info:
                await EleWaterTicketCRUD(EleWaterTicket, self.db).ele_ticket_sub(
                    self.order_info.order_no,
                    self.order_info.store_id,
                    self.order_info.customer_id,
                    ticket_info)

            return True

        except Exception:
            traceback.print_exc()
            raise Exception({
                "detail": f"电子水票扣除失败-001"
            })

    async def water_ticket_allocate(self):
        """
        根据订单套餐分配水票
        """
        try:
            if not self.order_info.order_water_ticket_goods_list:
                return True
            for water_ticket_package in self.order_info.order_water_ticket_goods_list:
                water_ticket_package_info = await self.db.get(WaterPackage, water_ticket_package.water_package_id)

                await EleWaterTicketService(self.db).ele_allocate(
                    BuyTicket(
                        water_ticket_id = water_ticket_package_info.target_water_ticket_id,
                        customer_id = self.order_info.customer_id,
                        address_id = self.order_info.customer_address.id,
                        num = water_ticket_package_info.num * water_ticket_package.quantity,
                        order_no = self.order_info.order_no,
                        ticket_category = 1
                    )
                )

            await self.db.commit()

            return True

        except Exception as e:
            traceback.print_exc()
            await self.db.rollback()
            if isinstance(e.args, tuple) and isinstance(e.args[0], dict) and e.args[0].get("detail"):
                raise Exception({
                    "detail": e.args[0].get("detail"),
                    "exception": e
                })
            raise Exception({
                "detail": f"根据订单套餐分配水票失败-001",
                "exception": e
            })


# if __name__ == "__main__":
#     import asyncio
#     from common.database import async_get_db
#
#     async def main():
#         # 获取数据库会话
#         async for db in async_get_db():
#             service = ProcessOrderAction(db, **{})
#             await service.process_state()
#
#             break  # 从生成器中获取一次 db 实例后退出
#
#     asyncio.run(main())


    # async def paper_water_ticket_sub(self):
    #     """
    #     纸质水票扣除
    #     {"id": 2, "num": 1, "type": 2, "code": 213}
    #     """
    #     ticket_info = []
    #     for water_ticket_obj in self.order_info.order_water_ticket_schema_list:
    #         if not water_ticket_obj.water_ticket_type:
    #             ticket_info.append({
    #                 "id": water_ticket_obj.water_ticket_id,
    #                 "num": water_ticket_obj.num,
    #                 "type": 2,
    #                 "code": water_ticket_obj.code
    #             })
    #     if not ticket_info:
    #         # 没有纸质水票
    #         return True
    #
    #     paper_ticket_info = ticket_info
    #
    #     # 扣除纸质水票
    #     if paper_ticket_info:
    #         await WaterTicketCodeCRUD(WaterTicketCode, self.db).paper_ticket_sub(
    #             self.order_info.store_id,
    #             self.order_info.customer_id,
    #             paper_ticket_info)
    #
    #     return True


# async def cancel_order(db: AsyncSession, order_no: str) -> bool:
#     """
#     水票订单按照订单号取消 取消订单   水票订单已付款不允许取消
#     """
#     # 1:待付款、2:待配送、3:配送中、4:已完成、5:已取消、6:已退款、7:异常订单
#     stmt = select(WaterOrder.ticket_type).where(WaterOrder.order_no == order_no, WaterOrder.status == 1).limit(1)
#     order = await db.execute(stmt)
#     ticket_type = order.scalar_one_or_none()
#     if not ticket_type:
#         raise ValueError(f"订单 {order_no} 不能取消！请检查订单！")
#
#     # 水票不允许取消
#     # if ticket_type == 2:
#     #     # 纸质水票取消 + 订单状态改变
#     #     await WaterTicketCodeCRUD(WaterTicketCode, db).cancel(order_no, 5)
#     # if ticket_type == 1:
#     #     # 电子水票取消 + 订单状态改变
#     #     await EleWaterTicketCodeCRUD(EleWaterTicketCode, db).cancel(order_no, 5)
#
#     return True

# if __name__ == "__main__":
#     ues_bucket_dict = {1:1}
#     return_bucket_dict = {1:1}
#
#     add_dict = {}
#     sub_dict = {}
#     # 遍历商品桶
#     # 回桶数量少于商品桶是增加借桶
#     # 回桶数量大于于商品桶是减少借桶
#     for goods_bucket_id, num in ues_bucket_dict.items():
#         return_bucket_num = return_bucket_dict.get(goods_bucket_id)
#         if return_bucket_num:
#             difference = num - return_bucket_num
#             if difference == 0:
#                 continue
#             if difference > 0:
#                 # 回桶少于商品桶是借桶
#                 add_dict[goods_bucket_id] = difference
#             else:
#                 sub_dict[goods_bucket_id] = return_bucket_num - num
#         else:
#             # 没有回桶就是借桶
#             add_dict[goods_bucket_id] = num
#
#     # 遍历回桶数据
#     # 回桶数量少于商品桶是增加借桶
#     # 回桶数量大于于商品桶是减少借桶
#     for return_bucket_id, num in return_bucket_dict.items():
#         if not ues_bucket_dict.get(return_bucket_id):
#             # 如果回桶数据不存在商品数据里  那么直接算回桶数据
#             sub_dict[return_bucket_id] = num
#         # 如果在商品数据里 上面已经处理过
#     print()