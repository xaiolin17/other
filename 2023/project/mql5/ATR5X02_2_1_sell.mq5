//+------------------------------------------------------------------+
//|                                                     .mq5 |
//|                                  Copyright 2023, MetaQuotes Ltd. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#include <GetAllData\StructAll.mqh>
#include <GetAllData\DataSaveAll.mqh>
#include <GetAllData\CurrentAssignmentStruct.mqh>
#include <GetAllData\AssignmentCycle.mqh>

input double lotss=0.01;        // 交易量手数
input ulong  EXPERT_MAGIC=123456;  // EA幻数
//shift
int kdata_shift_num = 1;
//count
int copy_count_num =  20;
//历史最大最小值
double history_min_0 = 0;
double history_max_0 = 0;
double high_history_arr[];
double low_history_arr[];

double history_M15_min_0 = 0;
double history_M15_max_0 = 0;
double high_history_M15_arr[];
double low_history_M15_arr[];

double history_M30_min_0 = 0;
double history_M30_max_0 = 0;
double high_history_M30_arr[];
double low_history_M30_arr[];

double history_H1_min_0 = 0;
double history_H1_max_0 = 0;
double high_history_H1_arr[];
double low_history_H1_arr[];

double history_D1_min_0 = 0;
double history_D1_max_0 = 0;
double high_history_D1_arr[];
double low_history_D1_arr[];
// 声明K线数据数组
KCandle KData_struct_arr[];

CycleData Cycle15M_struct_arr[];
CycleData Cycle30M_struct_arr[];
CycleData Cycle1H_struct_arr[];
CycleData Cycle1D_struct_arr[];
//交易量
double trade_lot;
//时间变化判断
datetime time_change = TimeCurrent();
//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {

//--- 设置正确的交易量
   double min_lot = SymbolInfoDouble(_Symbol,SYMBOL_VOLUME_MIN);
   trade_lot=lotss > min_lot ? lotss:min_lot;


   return(INIT_SUCCEEDED);
  }

//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
   Print("结束操作");
//获取交割单
   getHistoryDealsData("HistoryDealsDataTable_ATR5X02_2_1_sell.csv");

  }

//+------------------------------------------------------------------+
//|                     卖请求                                       |
//+------------------------------------------------------------------+
bool sell()
  {
   MqlTradeRequest request= {};
   MqlTradeResult  result= {};
   
   double atr_arr[];
   ATR(atr_arr,_Symbol,PERIOD_D1,5,copy_count_num);

//request.position =0;                // 关闭情况下的持仓单号
   request.action=TRADE_ACTION_DEAL;         // 设置开单
   request.symbol=Symbol();                      // 交易品种
   request.volume=trade_lot;                      // 交易量
   request.price=SymbolInfoDouble(Symbol(),SYMBOL_BID);
   request.sl= NormalizeDouble(request.price + atr_arr[1]*0.2,_Digits);
   request.tp= NormalizeDouble(request.price - atr_arr[1]*0.2*2,_Digits);
   request.deviation=0;                        // 可允许的价格偏差
   request.type=ORDER_TYPE_SELL_LIMIT;                // 订单类型
   request.type_filling=ORDER_FILLING_IOC;
   request.magic=EXPERT_MAGIC;            // 交易的幻数

   printf("发送交易请求:\n买入价格 %f, 止损 %f, 止盈 %f",request.price,request.sl,request.tp);
//--- 发送交易请求
   if(!OrderSend(request,result))
     {
      //--- 显示数据失败
      PrintFormat("OrderSend %s %s %.2f at %.5f error %d",request.symbol,ORDER_TYPE_BUY,trade_lot,request.price,GetLastError());

     }
//--- 交易请求结束
   return true;
  }

//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
//判定时间变动
   datetime time_change_tick = iTime(NULL,PERIOD_CURRENT,0);
   if(time_change == time_change_tick)
     {
      return;
     }
    // Print("iOpen(Symbol(), PERIOD_CURRENT, 1)    ===== ",iOpen(Symbol(), PERIOD_CURRENT, 1));
   time_change = time_change_tick;

//进行买操作
   bool buyType = sell();


   printf("单次请求结束------------------------");
  }

//+------------------------------------------------------------------+
void OnTrade()
  {

  }
//+------------------------------------------------------------------+
