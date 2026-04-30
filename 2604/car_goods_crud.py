from typing import TypeVar, Generic, Type, Optional
from pydantic import BaseModel
from sqlalchemy import select, delete, func, or_, and_
from sqlalchemy.ext.asyncio import AsyncSession
from module.brand.models.brand_model import Brand
from module.car.modules.car_module import Car
from module.category.models.category_model import Category
from module.goods.cruds.inventory_total_crud import GoodsTotalCRUD
from module.goods.modules.goods_module import Goods
from module.goods.modules.inventory_total_module import GoodsTotal
from module.goods.modules.record_module import CarGoodsRecord, StoreGoodsRecord
from module.goods.schemas.car_goods_schema import CarGoodsResponse, SummaryCarGoodsResponse
from module.goods.schemas.inventory_total_schema import GoodsTotalCreate
from module.user.models.user_expand_model import UserExpandModel
from module.user.models.user_model import UserModel


ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CarGoodsCRUD(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], db: AsyncSession):
        self.model = model
        self.db = db

    async def replenish_goods(self, goods_info: CreateSchemaType, user_id: int) -> Optional[ModelType]:
        """
        配送车补充商品
        需要在调用方 commit()

        查询车里是否有商品数据
        有  库存增加 ++
        否  新增数据

        构建数据库模型对象并持久化到数据库。若操作成功，返回创建的模型实例；
        若发生数据库异常，则回滚事务并返回 None。

        Args:
            goods_info (CreateSchemaType): 包含商品创建数据的 Pydantic 模型实例
            user_id

        Returns:
            Optional[ModelType]: 创建成功时返回数据库模型对象，失败时返回 None
        """
        try:
            """
            store_id: Optional[int] = Field(None, description="店铺ID")
            car_id: Optional[int] = Field(None, description="车ID")
            goods_id: Optional[int] = Field(None, description="商品ID")
            stock: Optional[int] = Field(None, description="库存数量，必须为非负整数")
            """
            # + 记录
            user_expand_info, user_info = None, None
            operator_result = None
            if user_id:
                user_expand_info = await self.db.get(UserExpandModel, user_id)

                user_info = await self.db.get(UserModel, user_id)
                if user_expand_info and user_expand_info.name:
                    operator_result = user_expand_info.name
                elif user_info and user_info.nick_name:
                    operator_result = user_info.nick_name


            old_stmt = select(self.model).where(
                self.model.store_id == goods_info.store_id,
                self.model.car_id == goods_info.car_id,
                self.model.goods_id == goods_info.goods_id
            )
            result = await self.db.execute(old_stmt)
            _obj = result.scalar_one_or_none()
            if not _obj:
                # 新增数据
                # 构建数据库模型对象并保存
                db_obj = self.model(**goods_info.model_dump())
                self.db.add(db_obj)

                # 新增商品日志
                await CreateCarGoodsLogCRUD(self.db).log_create(goods_info, operator_result, user_expand_info.user_id)

                # 查询总库存是否数据
                goods_total_stmt = select(GoodsTotal).where(
                    GoodsTotal.store_id==goods_info.store_id,
                    GoodsTotal.goods_id == goods_info.goods_id
                )
                goods_total_result = await self.db.execute(goods_total_stmt)
                goods_total_obj = goods_total_result.scalar_one_or_none()
                if not goods_total_obj:
                    # + 总库存
                    await GoodsTotalCRUD(GoodsTotal, self.db).create(
                        GoodsTotalCreate(
                            store_id=goods_info.store_id,
                            goods_id=goods_info.goods_id,
                            stock=goods_info.stock
                        )
                    )
            else:
                # 库存增加
                end_stock = _obj.stock + goods_info.stock

                self.db.add(
                    CarGoodsRecord(
                        store_id=_obj.store_id,
                        car_id=_obj.car_id,
                        goods_id=_obj.goods_id,
                        stock_initial=_obj.stock,
                        action="增加商品",
                        action_id=401,
                        stock_change=goods_info.stock,
                        stock_completion=end_stock,
                        operator=operator_result,
                        operator_id=user_id
                    )
                )

                _obj.stock = end_stock

            # 查询店铺
            goods_store_stmt = select(Goods).where(
                Goods.store_id == goods_info.store_id,
                Goods.id == goods_info.goods_id
            )
            goods_store_result = await self.db.execute(goods_store_stmt)
            goods_store_obj = goods_store_result.scalar_one_or_none()

            # 店铺库存扣除记录
            self.db.add(
                StoreGoodsRecord(
                    store_id=goods_info.store_id,
                    goods_id=goods_info.goods_id,
                    stock_initial=goods_store_obj.stock,
                    action="库存转移到车辆",
                    action_id=401,
                    stock_change=goods_info.stock,
                    stock_completion=goods_store_obj.stock - goods_info.stock,
                    operator=operator_result,
                    operator_id=user_expand_info.user_id
                )
            )

            # 减店铺库存
            goods_store_obj.stock -= goods_info.stock

            return True

        except Exception as e:
            await self.db.rollback()
            if isinstance(e.args, tuple) and isinstance(e.args[0], dict) and e.args[0].get("detail"):
                raise Exception({
                    "detail": e.args[0].get("detail"),
                    "exception": e
                })
            raise Exception({
                "detail": f"发生数据库错误",
                "exception": e
            })


    async def create(self, goods_info: CreateSchemaType) -> Optional[ModelType]:
        """
        创建
        需要在调用方 commit()

        构建数据库模型对象并持久化到数据库。若操作成功，返回创建的模型实例；
        若发生数据库异常，则回滚事务并返回 None。

        Args:
            goods_info (CreateSchemaType): 包含商品创建数据的 Pydantic 模型实例

        Returns:
            Optional[ModelType]: 创建成功时返回数据库模型对象，失败时返回 None
        """
        try:
            # 构建数据库模型对象并保存
            db_obj = self.model(**goods_info.model_dump())
            self.db.add(db_obj)
            return True

        except Exception as e:
            await self.db.rollback()
            if isinstance(e.args, tuple) and isinstance(e.args[0], dict) and e.args[0].get("detail"):
                raise Exception({
                    "detail": e.args[0].get("detail"),
                    "exception": e
                })
            raise Exception({
                "detail": f"创建时发生数据库错误",
                "exception": e
            })

    async def delete(self, _id: int) -> bool:
        """
        根据主键 ID 删除指定模型实例。

        使用直接 DELETE 语句删除，不预先加载对象，性能较高。
        若记录不存在，不报错，仅返回 False。
        若发生数据库错误，捕获异常并回滚事务，确保数据一致性。

        Args:
            _id (int): 待删除记录的主键 ID

        Returns:
            bool: 删除至少一行时返回 True（即记录存在并被删除），否则返回 False
        """
        stmt = delete(self.model).where(self.model.id == _id)
        try:
            result = await self.db.execute(stmt)
            return result.rowcount

        except Exception as e:
            await self.db.rollback()
            if isinstance(e.args, tuple) and isinstance(e.args[0], dict) and e.args[0].get("detail"):
                raise Exception({
                    "detail": e.args[0].get("detail"),
                    "exception": e
                })
            raise Exception({
                "detail": f"删除时发生数据库错误",
                "exception": e
            })

    async def replace_null(self, db_obj):
        if db_obj.brand_name is None:
            brand = select(Brand.name).where(Brand.id == db_obj.brand)
            brand_result = await self.db.execute(brand)
            brand_name = brand_result.scalar_one_or_none()
            if brand_name:
                db_obj.brand_name = brand_name
        if db_obj.type_name is None:
            category = select(Category.name).where(Category.id == db_obj.type)
            category_result = await self.db.execute(category)
            category_name = category_result.scalar_one_or_none()
            if category_name:
                db_obj.type_name = category_name

    async def replace_null_list(self, items):
        for db_obj in items:
            await self.replace_null(db_obj)
        return items

    async def get_by_id(self, _id: int) -> Optional[ModelType]:
        """
        根据主键 ID 查询 CarGoods，并关联 Goods 表补充信息

        Args:
            _id (int): CarGoods 的主键 ID

        Returns:
            dict: 包含 CarGoods 所有字段，并从 Goods 补充了额外信息的字典
        """
        # 获取 CarGoods 的所有列名
        car_goods_columns = {column.name for column in self.model.__table__.columns}

        # 构建 Goods 字段列表，排除 CarGoods 中已有的字段
        goods_fields = []
        for column in Goods.__table__.columns:
            if column.name not in car_goods_columns:
                goods_fields.append(getattr(Goods, column.name).label(f"goods_{column.name}"))

        # 如果没有需要补充的字段，直接查询 CarGoods
        if not goods_fields:
            stmt = select(self.model).where(self.model.id == _id)
            result = await self.db.execute(stmt)
            car_goods = result.scalar_one_or_none()

            if not car_goods:
                return None

            return {
                column.name: getattr(car_goods, column.name)
                for column in self.model.__table__.columns
            }

        # 查询 CarGoods 和 Goods 的补充字段
        stmt = select(
            self.model,
            *goods_fields
        ).join(
            Goods, self.model.id == Goods.id
        ).where(
            self.model.id == _id,
            Goods.is_deleted == False
        )

        result = await self.db.execute(stmt)
        record = result.one_or_none()

        if not record:
            return None

        # 分离 CarGoods 对象和 Goods 的额外字段
        car_goods = record[0]
        goods_field_values = record[1:]

        # 将 CarGoods 对象转换为字典
        result_dict = {
            column.name: getattr(car_goods, column.name)
            for column in self.model.__table__.columns
        }

        # 添加 Goods 的额外字段到结果中
        for field, value in zip(goods_fields, goods_field_values):
            # 提取字段名（去掉 'goods_' 前缀）
            field_name = str(field).split('.')[1].replace('_label_goods_', '')
            result_dict[field_name] = value

        return CarGoodsResponse(**result_dict)

    async def search_paginated_list(
            self,
            page_num: int = 1,
            page_size: int = 10,
            store_id: Optional[int] = None,
            car_id: Optional[int] = None,
            sort_field: str = "id",
            sort_order: str = "desc",
    ) -> tuple:
        """
        page_num: int = Query(1, description="当前页码，从1开始", ge=1)
        page_size: int = Query(10, description="每页数量，范围1-100", ge=1, le=100)
        store_id: Optional[int] = Query(None, description="店铺ID，用于筛选特定店铺的商品")
        car_id: Optional[int] = Query(None, description="车ID，用于筛选特车辆的商品")
        sort_field: str = Query("id", description="排序字段，仅支持允许的字段（如 id, name, price, stock）")
        sort_order: str = Query("desc", description="排序顺序，desc为降序，其他值为升序")

        Args:
            page_num:
            page_size:
            store_id:
            car_id:
            sort_field:
            sort_order:

        Returns:

        """
        # 校验分页参数
        if page_num < 1:
            page_num = 1
        if page_size < 1:
            page_size = 10
        elif page_size > 1000:
            page_size = 1000

        # 主表为 CarGoods，关联 Goods 获取商品详情
        stmt = (
            select(self.model, Goods, Car)
            .join(Goods, and_(self.model.goods_id == Goods.id, Goods.is_deleted == False), isouter=False)
            .join(Car, and_(self.model.car_id == Car.id), isouter=False)
        )

        # 添加过滤条件（全部附加到 WHERE）
        filters = [self.model.stock > 0]
        if store_id:
            filters.append(Goods.store_id == store_id)
        if car_id:
            filters.append(self.model.car_id == car_id)

        if filters:
            stmt = stmt.where(and_(*filters))

        # 排序字段白名单：注意 stock 直接来自 CarGoods
        allowed_sort_fields = {
            "id": Goods.id,
            "stock": self.model.stock,  # 使用 CarGoods 的库存
            "virtual_sales": Goods.virtual_sales,
        }
        sort_col = allowed_sort_fields.get(sort_field, Goods.id)

        if sort_order == "desc":
            stmt = stmt.order_by(sort_col.desc())
        else:
            stmt = stmt.order_by(sort_col.asc())

        # 总数查询
        count_stmt = select(func.count()).select_from(stmt.subquery())
        total = (await self.db.execute(count_stmt)).scalar() or 0

        # 分页
        stmt = stmt.offset((page_num - 1) * page_size).limit(page_size)
        result = await self.db.execute(stmt)
        rows = result.fetchall()

        # 构造返回对象列表
        items = []
        for row in rows:
            goods_total = row.CarGoods if hasattr(row, 'CarGoods') else row[0]
            goods = row.Goods if hasattr(row, 'Goods') else (row[1] if len(row) > 1 else None)
            car = row.Car if hasattr(row, 'Car') else (row[2] if len(row) > 2 else None)

            if goods:
                # 用 CarGoods 的 stock 覆盖 Goods 的 stock
                goods.stock = goods_total.stock or 0
                goods.car_id = goods_total.car_id
                goods.goods_id = goods_total.goods_id
                goods.plate_number = car.plate_number
                items.append(goods)

        items = await self.replace_null_list(items)

        return total, items, page_num, page_size

    async def summary_car_goods(
            self,
            store_id: int = None,
            car_ids: list = None,
            sort_field: str = "id",
            sort_order: str = "desc",
    ) -> tuple:
        """
        car_ids
        车ID列表
        """
        # 主表为 CarGoods，关联 Goods 获取商品详情
        stmt = (
            select(self.model, Goods)
            .join(Goods, and_(self.model.goods_id == Goods.id, Goods.is_deleted == False), isouter=False)
        )

        # 添加过滤条件（全部附加到 WHERE）
        filters = [self.model.stock > 0]
        if store_id:
            filters.append(Goods.store_id == store_id)
        if car_ids:
            filters.append(self.model.car_id.in_(car_ids))

        if filters:
            stmt = stmt.where(and_(*filters))

        # 排序字段白名单：注意 stock 直接来自 CarGoods
        allowed_sort_fields = {
            "id": Goods.id,
            "stock": self.model.stock,  # 使用 CarGoods 的库存
            "virtual_sales": Goods.virtual_sales,
        }
        sort_col = allowed_sort_fields.get(sort_field, Goods.id)

        if sort_order == "desc":
            stmt = stmt.order_by(sort_col.desc())
        else:
            stmt = stmt.order_by(sort_col.asc())

        # 总数查询
        count_stmt = select(func.count()).select_from(stmt.subquery())
        total = (await self.db.execute(count_stmt)).scalar() or 0


        result = await self.db.execute(stmt)
        rows = result.fetchall()

        # 构造返回对象列表
        items = []
        for row in rows:
            goods_total = row.CarGoods if hasattr(row, 'CarGoods') else row[0]
            goods = row.Goods if hasattr(row, 'Goods') else (row[1] if len(row) > 1 else None)

            if goods:
                # 用 CarGoods 的 stock 覆盖 Goods 的 stock
                goods.stock = goods_total.stock or 0
                goods.car_id = goods_total.car_id
                goods.goods_id = goods_total.goods_id
                items.append(goods)

        items = await self.replace_null_list(items)

        merged = {}
        for item in items:
            key = (item.goods_id, item.store_id)
            if key in merged:
                merged[key].stock += item.stock
            else:
                # 注意：需保留原对象，若后续可能修改可深拷贝，此处直接引用
                merged[key] = item

        items = list(merged.values())

        return total, items


"""
新增商品日志 CRUD
"""
class CreateCarGoodsLogCRUD:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def log_create(self, goods_obj, operator_result, user_id):
        self.db.add(
            CarGoodsRecord(
                store_id=goods_obj.store_id,
                car_id=goods_obj.car_id,
                goods_id=goods_obj.goods_id,
                stock_initial=0,
                action="新增商品",
                action_id=101,
                stock_change=goods_obj.stock,
                stock_completion=goods_obj.stock,
                operator=operator_result,
                operator_id=user_id
            )
        )


"""
删除商品日志 CRUD
"""
class DeleteCarGoodsLogCRUD:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def log_delete(self, goods_obj, operator_result, user_id):
        self.db.add(
            CarGoodsRecord(
                store_id=goods_obj.store_id,
                car_id=goods_obj.car_id,
                goods_id=goods_obj.goods_id,
                stock_initial=goods_obj.stock,
                action="删除商品",
                action_id=102,
                stock_change=goods_obj.stock,
                stock_completion=0,
                operator=operator_result,
                operator_id=user_id
            )
        )
