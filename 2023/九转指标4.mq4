//+------------------------------------------------------------------+
//|                                                           九转.mq4 |
//|                                                                  |
//|                                                                  |
//+------------------------------------------------------------------+
#property copyright ""
#property link      ""
#property version   "1.00"
#property strict
#property indicator_chart_window


enum TYPE{空心=129,实心=140};

input bool ALL=true;//显示所有序列
input ENUM_APPLIED_PRICE PRICE=PRICE_TYPICAL;//参考价格
input TYPE Type=实心;//序列类型
input int WIDTH=1;//序列大小
input color CLR_BUY=clrRed;//序列颜色
input color CLR_SELL=clrDeepSkyBlue;//序列颜色

input int Num=9;//反转

//+------------------------------------------------------------------+
//| Custom indicator initialization function                         |
//+------------------------------------------------------------------+

string FIXED="NINE_T_";

int OnInit()
  {
//--- indicator buffers mapping
   
//---
   return(INIT_SUCCEEDED);
  }
void OnDeinit(const int reason)
  {   
    DeleteObjects(FIXED);
  }
//+------------------------------------------------------------------+
//| Custom indicator iteration function                              |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[])
  {
//---
   int i,limit;
//--- check for bars count and input parameter
   if(rates_total<=Num)
      return(0);
//--- counting from 0 to rates_total

   ArraySetAsSeries(time,true);
   ArraySetAsSeries(close,true);
   ArraySetAsSeries(high,true);
   ArraySetAsSeries(low,true);
   
   if(prev_calculated==0)
      limit = 0;
   else
      limit=prev_calculated-1;
   
   int buy=0,sell=0,last=rates_total;
   string  name="";
   
   if(!ALL)
   {
      for(i=rates_total-5; i>0; i--)
      {
         if(iMA(NULL,0,1,0,MODE_EMA,PRICE,i)>iMA(NULL,0,1,0,MODE_EMA,PRICE,i+4))
         {
            buy++;
            if(buy==Num)
            {
               for(int j=0;j<buy;j++)
               {
                  name = StringFormat("%s_BUY_%s_%d",FIXED,TimeToString(time[i]),j+1);
                  ArrowCreate(0,name,0,time[i+Num-j-1],high[i+Num-j-1],Type+j,ANCHOR_BOTTOM,CLR_BUY,STYLE_SOLID,WIDTH);
               }
               buy=0;
            }
         }
         else
         {
            buy=0;
         }
         if(iMA(NULL,0,1,0,MODE_EMA,PRICE,i)<iMA(NULL,0,1,0,MODE_EMA,PRICE,i+4))
         {
            sell++;
            if(sell==Num)
            {
               for(int j=0;j<sell;j++)
               {
                  name = StringFormat("%s_SELL_%s_%d",FIXED,TimeToString(time[i]),j+1);
                  ArrowCreate(0,name,0,time[i+Num-j-1],low[i+Num-j-1],Type+j,ANCHOR_TOP,CLR_SELL,STYLE_SOLID,WIDTH);
               }
               sell=0;
            }
         }
         else
         {
            sell=0;
         }
      }
   }
   else
   {
      for(i=rates_total-5; i>0; i--)
      {
         if(close[i]>close[i+4])
         {
            name = StringFormat("%s_BUY_%s_%d",FIXED,TimeToString(time[i]),buy+1);
            ArrowCreate(0,name,0,time[i],high[i],Type+buy,ANCHOR_BOTTOM,CLR_BUY,STYLE_SOLID,WIDTH);
            
            buy++;
            if(buy==Num)
            {
               buy=0;
            }
         }
         else
         {
            buy=0;
         }
         if(close[i]<close[i+4])
         {
            name = StringFormat("%s_SELL_%s_%d",FIXED,TimeToString(time[i]),sell+1);
            ArrowCreate(0,name,0,time[i],low[i],Type+sell,ANCHOR_TOP,CLR_SELL,STYLE_SOLID,WIDTH);
            
            sell++;
            if(sell==Num)
            {
               sell=0;
            }
         }
         else
         {
            sell=0;
         }
      }
  }
//--- return value of prev_calculated for next call
   return(rates_total);
  }
//+------------------------------------------------------------------+
void DeleteObjects(string fixed)
{
   int len = StringLen(fixed);
   int i=0;

   while (i < ObjectsTotal(0,0))
   {
      string objName = ObjectName(0,i);
      if (StringSubstr(objName, 0, len) != fixed)
      {
         i++;
         continue;
      }
      ObjectDelete(0,objName);
   }
}
bool ArrowCreate(const long              chart_ID=0,           // chart's ID 
                 const string            name="Arrow",         // arrow name 
                 const int               sub_window=0,         // subwindow index 
                 datetime                time=0,               // anchor point time 
                 double                  price=0,              // anchor point price 
                 const uchar             arrow_code=128,       // arrow code 
                 const ENUM_ARROW_ANCHOR anchor=ANCHOR_BOTTOM, // anchor point position 
                 const color             clr=clrRed,           // arrow color 
                 const ENUM_LINE_STYLE   style=STYLE_SOLID,    // border line style 
                 const int               width=3,              // arrow size 
                 const bool              back=false,           // in the background 
                 const bool              selection=false,       // highlight to move 
                 const bool              hidden=true,          // hidden in the object list 
                 const long              z_order=0)            // priority for mouse click 
  { 
//--- reset the error value 
   ResetLastError(); 
//--- create an arrow 
   if(!ObjectCreate(chart_ID,name,OBJ_ARROW,sub_window,time,price)) 
     { 
      Print(__FUNCTION__, 
            ": failed to create an arrow! Error code = ",GetLastError()); 
      return(false); 
     } 
//--- set the arrow code 
   ObjectSetInteger(chart_ID,name,OBJPROP_ARROWCODE,arrow_code); 
//--- set anchor type 
   ObjectSetInteger(chart_ID,name,OBJPROP_ANCHOR,anchor); 
//--- set the arrow color 
   ObjectSetInteger(chart_ID,name,OBJPROP_COLOR,clr); 
//--- set the border line style 
   ObjectSetInteger(chart_ID,name,OBJPROP_STYLE,style); 
//--- set the arrow's size 
   ObjectSetInteger(chart_ID,name,OBJPROP_WIDTH,width); 
//--- display in the foreground (false) or background (true) 
   ObjectSetInteger(chart_ID,name,OBJPROP_BACK,back); 
//--- enable (true) or disable (false) the mode of moving the arrow by mouse 
//--- when creating a graphical object using ObjectCreate function, the object cannot be 
//--- highlighted and moved by default. Inside this method, selection parameter 
//--- is true by default making it possible to highlight and move the object 
   ObjectSetInteger(chart_ID,name,OBJPROP_SELECTABLE,selection); 
   ObjectSetInteger(chart_ID,name,OBJPROP_SELECTED,selection); 
//--- hide (true) or display (false) graphical object name in the object list 
   ObjectSetInteger(chart_ID,name,OBJPROP_HIDDEN,hidden); 
//--- set the priority for receiving the event of a mouse click in the chart 
   ObjectSetInteger(chart_ID,name,OBJPROP_ZORDER,z_order); 
//--- successful execution 
   return(true); 
  }