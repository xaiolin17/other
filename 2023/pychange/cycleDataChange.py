"""
cycleDataChange.py
1.读取二进制文件
2.解析二进制格式数据
3.转为DataFrame
"""
import struct
import pandas as pd
import datetime
from decimal import Decimal
def bin_to_cycleData(binary_file):
    # 定义二进制数据的解析格式
    data_format = ('qddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
                   'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
                   'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
                   'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
                   'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
                   'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
                   'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
                   'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
                   'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
                   'ddddddddd'
                   'BBBBBBBBBBBBBBBBBBBB'
                   'BBBBBBBBBBBBBBBBBBBB'
                   'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
                   'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
                   'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')  # 8字节整数g 8字节浮点数d
    print("二进制文件读取***")
    # 读取二进制文件并解析数据
    with open(binary_file, 'rb') as file:
        binary_data = file.read()
    # 存放数据
    data_list = []
    # 以每行数据所占长度取
    print(len(data_format))
    print('struct.calcsize(data_format)',struct.calcsize(data_format))
    for i in range(0, len(binary_data), struct.calcsize(data_format)):
        #按照解析格式取出各项
        unpacked_data = struct.unpack_from(data_format, binary_data, i)
        volume = unpacked_data[0]
        atr5 = round(unpacked_data[1], 4)
        atr10 = round(unpacked_data[2], 4)
        atr5_change1 = round(unpacked_data[3], 4)
        atr5_change2 = round(unpacked_data[4], 4)
        atr5_change3 = round(unpacked_data[5], 4)
        atr5_change4 = round(unpacked_data[6], 4)
        atr5_change5 = round(unpacked_data[7], 4)
        atr5_change6 = round(unpacked_data[8], 4)
        atr5_change7 = round(unpacked_data[9], 4)
        atr5_change8 = round(unpacked_data[10], 4)
        atr5_change9 = round(unpacked_data[11], 4)
        atr5_change10 = round(unpacked_data[12], 4)
        atr5_current_change1 = round(unpacked_data[13], 4)
        atr5_current_change2 = round(unpacked_data[14], 4)
        atr5_current_change3 = round(unpacked_data[15], 4)
        atr5_current_change4 = round(unpacked_data[16], 4)
        atr5_current_change5 = round(unpacked_data[17], 4)
        atr5_current_change6 = round(unpacked_data[18], 4)
        atr5_current_change7 = round(unpacked_data[19], 4)
        atr5_current_change8 = round(unpacked_data[20], 4)
        atr5_current_change9 = round(unpacked_data[21], 4)
        atr5_current_change10 = round(unpacked_data[22], 4)
        atr10_change1 = round(unpacked_data[23], 4)
        atr10_change2 = round(unpacked_data[24], 4)
        atr10_change3 = round(unpacked_data[25], 4)
        atr10_change4 = round(unpacked_data[26], 4)
        atr10_change5 = round(unpacked_data[27], 4)
        atr10_change6 = round(unpacked_data[28], 4)
        atr10_change7 = round(unpacked_data[29], 4)
        atr10_change8 = round(unpacked_data[30], 4)
        atr10_change9 = round(unpacked_data[31], 4)
        atr10_change10 = round(unpacked_data[32], 4)
        atr10_current_change1 = round(unpacked_data[33], 4)
        atr10_current_change2 = round(unpacked_data[34], 4)
        atr10_current_change3 = round(unpacked_data[35], 4)
        atr10_current_change4 = round(unpacked_data[36], 4)
        atr10_current_change5 = round(unpacked_data[37], 4)
        atr10_current_change6 = round(unpacked_data[38], 4)
        atr10_current_change7 = round(unpacked_data[39], 4)
        atr10_current_change8 = round(unpacked_data[40], 4)
        atr10_current_change9 = round(unpacked_data[41], 4)
        atr10_current_change10 = round(unpacked_data[42], 4)
        macd = round(unpacked_data[43], 4)
        macd_change1 = round(unpacked_data[44], 4)
        macd_change2 = round(unpacked_data[45], 4)
        macd_change3 = round(unpacked_data[46], 4)
        macd_change4 = round(unpacked_data[47], 4)
        macd_change5 = round(unpacked_data[48], 4)
        macd_change6 = round(unpacked_data[49], 4)
        macd_change7 = round(unpacked_data[50], 4)
        macd_change8 = round(unpacked_data[51], 4)
        macd_change9 = round(unpacked_data[52], 4)
        macd_change10 = round(unpacked_data[53], 4)
        macd_current_change1 = round(unpacked_data[54], 4)
        macd_current_change2 = round(unpacked_data[55], 4)
        macd_current_change3 = round(unpacked_data[56], 4)
        macd_current_change4 = round(unpacked_data[57], 4)
        macd_current_change5 = round(unpacked_data[58], 4)
        macd_current_change6 = round(unpacked_data[59], 4)
        macd_current_change7 = round(unpacked_data[60], 4)
        macd_current_change8 = round(unpacked_data[61], 4)
        macd_current_change9 = round(unpacked_data[62], 4)
        macd_current_change10 = round(unpacked_data[63], 4)
        sma5 = round(unpacked_data[64], 4)
        sma10 = round(unpacked_data[65], 4)
        sma5_change1 = round(unpacked_data[66], 4)
        sma5_change2 = round(unpacked_data[67], 4)
        sma5_change3 = round(unpacked_data[68], 4)
        sma5_change4 = round(unpacked_data[69], 4)
        sma5_change5 = round(unpacked_data[70], 4)
        sma5_change6 = round(unpacked_data[71], 4)
        sma5_change7 = round(unpacked_data[72], 4)
        sma5_change8 = round(unpacked_data[73], 4)
        sma5_change9 = round(unpacked_data[74], 4)
        sma5_change10 = round(unpacked_data[75], 4)
        sma5_current_change1 = round(unpacked_data[76], 4)
        sma5_current_change2 = round(unpacked_data[77], 4)
        sma5_current_change3 = round(unpacked_data[78], 4)
        sma5_current_change4 = round(unpacked_data[79], 4)
        sma5_current_change5 = round(unpacked_data[80], 4)
        sma5_current_change6 = round(unpacked_data[81], 4)
        sma5_current_change7 = round(unpacked_data[82], 4)
        sma5_current_change8 = round(unpacked_data[83], 4)
        sma5_current_change9 = round(unpacked_data[84], 4)
        sma5_current_change10 = round(unpacked_data[85], 4)
        sma10_change1 = round(unpacked_data[86], 4)
        sma10_change2 = round(unpacked_data[87], 4)
        sma10_change3 = round(unpacked_data[88], 4)
        sma10_change4 = round(unpacked_data[89], 4)
        sma10_change5 = round(unpacked_data[90], 4)
        sma10_change6 = round(unpacked_data[91], 4)
        sma10_change7 = round(unpacked_data[92], 4)
        sma10_change8 = round(unpacked_data[93], 4)
        sma10_change9 = round(unpacked_data[94], 4)
        sma10_change10 = round(unpacked_data[95], 4)
        sma10_current_change1 = round(unpacked_data[96], 4)
        sma10_current_change2 = round(unpacked_data[97], 4)
        sma10_current_change3 = round(unpacked_data[98], 4)
        sma10_current_change4 = round(unpacked_data[99], 4)
        sma10_current_change5 = round(unpacked_data[100], 4)
        sma10_current_change6 = round(unpacked_data[101], 4)
        sma10_current_change7 = round(unpacked_data[102], 4)
        sma10_current_change8 = round(unpacked_data[103], 4)
        sma10_current_change9 = round(unpacked_data[104], 4)
        sma10_current_change10 = round(unpacked_data[105], 4)
        ema5 = round(unpacked_data[106], 4)
        ema10 = round(unpacked_data[107], 4)
        ema5_change1 = round(unpacked_data[108], 4)
        ema5_change2 = round(unpacked_data[109], 4)
        ema5_change3 = round(unpacked_data[110], 4)
        ema5_change4 = round(unpacked_data[111], 4)
        ema5_change5 = round(unpacked_data[112], 4)
        ema5_change6 = round(unpacked_data[113], 4)
        ema5_change7 = round(unpacked_data[114], 4)
        ema5_change8 = round(unpacked_data[115], 4)
        ema5_change9 = round(unpacked_data[116], 4)
        ema5_change10 = round(unpacked_data[117], 4)
        ema5_current_change1 = round(unpacked_data[118], 4)
        ema5_current_change2 = round(unpacked_data[119], 4)
        ema5_current_change3 = round(unpacked_data[120], 4)
        ema5_current_change4 = round(unpacked_data[121], 4)
        ema5_current_change5 = round(unpacked_data[122], 4)
        ema5_current_change6 = round(unpacked_data[123], 4)
        ema5_current_change7 = round(unpacked_data[124], 4)
        ema5_current_change8 = round(unpacked_data[125], 4)
        ema5_current_change9 = round(unpacked_data[126], 4)
        ema5_current_change10 = round(unpacked_data[127], 4)
        ema10_change1 = round(unpacked_data[128], 4)
        ema10_change2 = round(unpacked_data[129], 4)
        ema10_change3 = round(unpacked_data[130], 4)
        ema10_change4 = round(unpacked_data[131], 4)
        ema10_change5 = round(unpacked_data[132], 4)
        ema10_change6 = round(unpacked_data[133], 4)
        ema10_change7 = round(unpacked_data[134], 4)
        ema10_change8 = round(unpacked_data[135], 4)
        ema10_change9 = round(unpacked_data[136], 4)
        ema10_change10 = round(unpacked_data[137], 4)
        ema10_current_change1 = round(unpacked_data[138], 4)
        ema10_current_change2 = round(unpacked_data[139], 4)
        ema10_current_change3 = round(unpacked_data[140], 4)
        ema10_current_change4 = round(unpacked_data[141], 4)
        ema10_current_change5 = round(unpacked_data[142], 4)
        ema10_current_change6 = round(unpacked_data[143], 4)
        ema10_current_change7 = round(unpacked_data[144], 4)
        ema10_current_change8 = round(unpacked_data[145], 4)
        ema10_current_change9 = round(unpacked_data[146], 4)
        ema10_current_change10 = round(unpacked_data[147], 4)
        smma5 = round(unpacked_data[148], 4)
        smma10 = round(unpacked_data[149], 4)
        smma5_change1 = round(unpacked_data[150], 4)
        smma5_change2 = round(unpacked_data[151], 4)
        smma5_change3 = round(unpacked_data[152], 4)
        smma5_change4 = round(unpacked_data[153], 4)
        smma5_change5 = round(unpacked_data[154], 4)
        smma5_change6 = round(unpacked_data[155], 4)
        smma5_change7 = round(unpacked_data[156], 4)
        smma5_change8 = round(unpacked_data[157], 4)
        smma5_change9 = round(unpacked_data[158], 4)
        smma5_change10 = round(unpacked_data[159], 4)
        smma5_current_change1 = round(unpacked_data[160], 4)
        smma5_current_change2 = round(unpacked_data[161], 4)
        smma5_current_change3 = round(unpacked_data[162], 4)
        smma5_current_change4 = round(unpacked_data[163], 4)
        smma5_current_change5 = round(unpacked_data[164], 4)
        smma5_current_change6 = round(unpacked_data[165], 4)
        smma5_current_change7 = round(unpacked_data[166], 4)
        smma5_current_change8 = round(unpacked_data[167], 4)
        smma5_current_change9 = round(unpacked_data[168], 4)
        smma5_current_change10 = round(unpacked_data[169], 4)
        smma10_change1 = round(unpacked_data[170], 4)
        smma10_change2 = round(unpacked_data[171], 4)
        smma10_change3 = round(unpacked_data[172], 4)
        smma10_change4 = round(unpacked_data[173], 4)
        smma10_change5 = round(unpacked_data[174], 4)
        smma10_change6 = round(unpacked_data[175], 4)
        smma10_change7 = round(unpacked_data[176], 4)
        smma10_change8 = round(unpacked_data[177], 4)
        smma10_change9 = round(unpacked_data[178], 4)
        smma10_change10 = round(unpacked_data[179], 4)
        smma10_current_change1 = round(unpacked_data[180], 4)
        smma10_current_change2 = round(unpacked_data[181], 4)
        smma10_current_change3 = round(unpacked_data[182], 4)
        smma10_current_change4 = round(unpacked_data[183], 4)
        smma10_current_change5 = round(unpacked_data[184], 4)
        smma10_current_change6 = round(unpacked_data[185], 4)
        smma10_current_change7 = round(unpacked_data[186], 4)
        smma10_current_change8 = round(unpacked_data[187], 4)
        smma10_current_change9 = round(unpacked_data[188], 4)
        smma10_current_change10 = round(unpacked_data[189], 4)
        lwma5 = round(unpacked_data[190], 4)
        lwma10 = round(unpacked_data[191], 4)
        lwma5_change1 = round(unpacked_data[192], 4)
        lwma5_change2 = round(unpacked_data[193], 4)
        lwma5_change3 = round(unpacked_data[194], 4)
        lwma5_change4 = round(unpacked_data[195], 4)
        lwma5_change5 = round(unpacked_data[196], 4)
        lwma5_change6 = round(unpacked_data[197], 4)
        lwma5_change7 = round(unpacked_data[198], 4)
        lwma5_change8 = round(unpacked_data[199], 4)
        lwma5_change9 = round(unpacked_data[200], 4)
        lwma5_change10 = round(unpacked_data[201], 4)
        lwma5_current_change1 = round(unpacked_data[202], 4)
        lwma5_current_change2 = round(unpacked_data[203], 4)
        lwma5_current_change3 = round(unpacked_data[204], 4)
        lwma5_current_change4 = round(unpacked_data[205], 4)
        lwma5_current_change5 = round(unpacked_data[206], 4)
        lwma5_current_change6 = round(unpacked_data[207], 4)
        lwma5_current_change7 = round(unpacked_data[208], 4)
        lwma5_current_change8 = round(unpacked_data[209], 4)
        lwma5_current_change9 = round(unpacked_data[210], 4)
        lwma5_current_change10 = round(unpacked_data[211], 4)
        lwma10_change1 = round(unpacked_data[212], 4)
        lwma10_change2 = round(unpacked_data[213], 4)
        lwma10_change3 = round(unpacked_data[214], 4)
        lwma10_change4 = round(unpacked_data[215], 4)
        lwma10_change5 = round(unpacked_data[216], 4)
        lwma10_change6 = round(unpacked_data[217], 4)
        lwma10_change7 = round(unpacked_data[218], 4)
        lwma10_change8 = round(unpacked_data[219], 4)
        lwma10_change9 = round(unpacked_data[220], 4)
        lwma10_change10 = round(unpacked_data[221], 4)
        lwma10_current_change1 = round(unpacked_data[222], 4)
        lwma10_current_change2 = round(unpacked_data[223], 4)
        lwma10_current_change3 = round(unpacked_data[224], 4)
        lwma10_current_change4 = round(unpacked_data[225], 4)
        lwma10_current_change5 = round(unpacked_data[226], 4)
        lwma10_current_change6 = round(unpacked_data[227], 4)
        lwma10_current_change7 = round(unpacked_data[228], 4)
        lwma10_current_change8 = round(unpacked_data[229], 4)
        lwma10_current_change9 = round(unpacked_data[230], 4)
        lwma10_current_change10 = round(unpacked_data[231], 4)
        rsi5 = round(unpacked_data[232], 4)
        rsi14 = round(unpacked_data[233], 4)
        rsi5_change1 = round(unpacked_data[234], 4)
        rsi5_change2 = round(unpacked_data[235], 4)
        rsi5_change3 = round(unpacked_data[236], 4)
        rsi5_change4 = round(unpacked_data[237], 4)
        rsi5_change5 = round(unpacked_data[238], 4)
        rsi5_change6 = round(unpacked_data[239], 4)
        rsi5_change7 = round(unpacked_data[240], 4)
        rsi5_change8 = round(unpacked_data[241], 4)
        rsi5_change9 = round(unpacked_data[242], 4)
        rsi5_change10 = round(unpacked_data[243], 4)
        rsi5_current_change1 = round(unpacked_data[244], 4)
        rsi5_current_change2 = round(unpacked_data[245], 4)
        rsi5_current_change3 = round(unpacked_data[246], 4)
        rsi5_current_change4 = round(unpacked_data[247], 4)
        rsi5_current_change5 = round(unpacked_data[248], 4)
        rsi5_current_change6 = round(unpacked_data[249], 4)
        rsi5_current_change7 = round(unpacked_data[250], 4)
        rsi5_current_change8 = round(unpacked_data[251], 4)
        rsi5_current_change9 = round(unpacked_data[252], 4)
        rsi5_current_change10 = round(unpacked_data[253], 4)
        rsi14_change1 = round(unpacked_data[254], 4)
        rsi14_change2 = round(unpacked_data[255], 4)
        rsi14_change3 = round(unpacked_data[256], 4)
        rsi14_change4 = round(unpacked_data[257], 4)
        rsi14_change5 = round(unpacked_data[258], 4)
        rsi14_change6 = round(unpacked_data[259], 4)
        rsi14_change7 = round(unpacked_data[260], 4)
        rsi14_change8 = round(unpacked_data[261], 4)
        rsi14_change9 = round(unpacked_data[262], 4)
        rsi14_change10 = round(unpacked_data[263], 4)
        rsi14_current_change1 = round(unpacked_data[264], 4)
        rsi14_current_change2 = round(unpacked_data[265], 4)
        rsi14_current_change3 = round(unpacked_data[266], 4)
        rsi14_current_change4 = round(unpacked_data[267], 4)
        rsi14_current_change5 = round(unpacked_data[268], 4)
        rsi14_current_change6 = round(unpacked_data[269], 4)
        rsi14_current_change7 = round(unpacked_data[270], 4)
        rsi14_current_change8 = round(unpacked_data[271], 4)
        rsi14_current_change9 = round(unpacked_data[272], 4)
        rsi14_current_change10 = round(unpacked_data[273], 4)
        sar = round(unpacked_data[274], 4)
        sar_change1 = round(unpacked_data[275], 4)
        sar_change2 = round(unpacked_data[276], 4)
        sar_change3 = round(unpacked_data[277], 4)
        sar_change4 = round(unpacked_data[278], 4)
        sar_change5 = round(unpacked_data[279], 4)
        sar_change6 = round(unpacked_data[280], 4)
        sar_change7 = round(unpacked_data[281], 4)
        sar_change8 = round(unpacked_data[282], 4)
        sar_change9 = round(unpacked_data[283], 4)
        sar_change10 = round(unpacked_data[284], 4)
        sar_current_change1 = round(unpacked_data[285], 4)
        sar_current_change2 = round(unpacked_data[286], 4)
        sar_current_change3 = round(unpacked_data[287], 4)
        sar_current_change4 = round(unpacked_data[288], 4)
        sar_current_change5 = round(unpacked_data[289], 4)
        sar_current_change6 = round(unpacked_data[290], 4)
        sar_current_change7 = round(unpacked_data[291], 4)
        sar_current_change8 = round(unpacked_data[292], 4)
        sar_current_change9 = round(unpacked_data[293], 4)
        sar_current_change10 = round(unpacked_data[294], 4)
        adx = round(unpacked_data[295], 4)
        adx_DI_plus = round(unpacked_data[296], 4)
        adx_DI_minus = round(unpacked_data[297], 4)
        adx_change1 = round(unpacked_data[298], 4)
        adx_change2 = round(unpacked_data[299], 4)
        adx_change3 = round(unpacked_data[300], 4)
        adx_change4 = round(unpacked_data[301], 4)
        adx_change5 = round(unpacked_data[302], 4)
        adx_change6 = round(unpacked_data[303], 4)
        adx_change7 = round(unpacked_data[304], 4)
        adx_change8 = round(unpacked_data[305], 4)
        adx_change9 = round(unpacked_data[306], 4)
        adx_change10 = round(unpacked_data[307], 4)
        adx_current_change1 = round(unpacked_data[308], 4)
        adx_current_change2 = round(unpacked_data[309], 4)
        adx_current_change3 = round(unpacked_data[310], 4)
        adx_current_change4 = round(unpacked_data[311], 4)
        adx_current_change5 = round(unpacked_data[312], 4)
        adx_current_change6 = round(unpacked_data[313], 4)
        adx_current_change7 = round(unpacked_data[314], 4)
        adx_current_change8 = round(unpacked_data[315], 4)
        adx_current_change9 = round(unpacked_data[316], 4)
        adx_current_change10 = round(unpacked_data[317], 4)
        cci = round(unpacked_data[318], 4)
        cci_change1 = round(unpacked_data[319], 4)
        cci_change2 = round(unpacked_data[320], 4)
        cci_change3 = round(unpacked_data[321], 4)
        cci_change4 = round(unpacked_data[322], 4)
        cci_change5 = round(unpacked_data[323], 4)
        cci_change6 = round(unpacked_data[324], 4)
        cci_change7 = round(unpacked_data[325], 4)
        cci_change8 = round(unpacked_data[326], 4)
        cci_change9 = round(unpacked_data[327], 4)
        cci_change10 = round(unpacked_data[328], 4)
        cci_current_change1 = round(unpacked_data[329], 4)
        cci_current_change2 = round(unpacked_data[330], 4)
        cci_current_change3 = round(unpacked_data[331], 4)
        cci_current_change4 = round(unpacked_data[332], 4)
        cci_current_change5 = round(unpacked_data[333], 4)
        cci_current_change6 = round(unpacked_data[334], 4)
        cci_current_change7 = round(unpacked_data[335], 4)
        cci_current_change8 = round(unpacked_data[336], 4)
        cci_current_change9 = round(unpacked_data[337], 4)
        cci_current_change10 = round(unpacked_data[338], 4)
        slowk = round(unpacked_data[339], 4)
        slowd = round(unpacked_data[340], 4)
        slowk_change1 = round(unpacked_data[341], 4)
        slowk_change2 = round(unpacked_data[342], 4)
        slowk_change3 = round(unpacked_data[343], 4)
        slowk_change4 = round(unpacked_data[344], 4)
        slowk_change5 = round(unpacked_data[345], 4)
        slowk_change6 = round(unpacked_data[346], 4)
        slowk_change7 = round(unpacked_data[347], 4)
        slowk_change8 = round(unpacked_data[348], 4)
        slowk_change9 = round(unpacked_data[349], 4)
        slowk_change10 = round(unpacked_data[350], 4)
        slowk_current_change1 = round(unpacked_data[351], 4)
        slowk_current_change2 = round(unpacked_data[352], 4)
        slowk_current_change3 = round(unpacked_data[353], 4)
        slowk_current_change4 = round(unpacked_data[354], 4)
        slowk_current_change5 = round(unpacked_data[355], 4)
        slowk_current_change6 = round(unpacked_data[356], 4)
        slowk_current_change7 = round(unpacked_data[357], 4)
        slowk_current_change8 = round(unpacked_data[358], 4)
        slowk_current_change9 = round(unpacked_data[359], 4)
        slowk_current_change10 = round(unpacked_data[360], 4)
        boll_upper_band = round(unpacked_data[361], 4)
        boll_middle_band = round(unpacked_data[362], 4)
        boll_lower_band = round(unpacked_data[363], 4)
        boll_change1 = round(unpacked_data[364], 4)
        boll_change2 = round(unpacked_data[365], 4)
        boll_change3 = round(unpacked_data[366], 4)
        boll_change4 = round(unpacked_data[367], 4)
        boll_change5 = round(unpacked_data[368], 4)
        boll_change6 = round(unpacked_data[369], 4)
        boll_change7 = round(unpacked_data[370], 4)
        boll_change8 = round(unpacked_data[371], 4)
        boll_change9 = round(unpacked_data[372], 4)
        boll_change10 = round(unpacked_data[373], 4)
        boll_current_change1 = round(unpacked_data[374], 4)
        boll_current_change2 = round(unpacked_data[375], 4)
        boll_current_change3 = round(unpacked_data[376], 4)
        boll_current_change4 = round(unpacked_data[377], 4)
        boll_current_change5 = round(unpacked_data[378], 4)
        boll_current_change6 = round(unpacked_data[379], 4)
        boll_current_change7 = round(unpacked_data[380], 4)
        boll_current_change8 = round(unpacked_data[381], 4)
        boll_current_change9 = round(unpacked_data[382], 4)
        boll_current_change10 = round(unpacked_data[383], 4)
        ac_value = round(unpacked_data[384], 4)
        ac_color = round(unpacked_data[385], 4)
        ac_change1 = round(unpacked_data[386], 4)
        ac_change2 = round(unpacked_data[387], 4)
        ac_change3 = round(unpacked_data[388], 4)
        ac_change4 = round(unpacked_data[389], 4)
        ac_change5 = round(unpacked_data[390], 4)
        ac_change6 = round(unpacked_data[391], 4)
        ac_change7 = round(unpacked_data[392], 4)
        ac_change8 = round(unpacked_data[393], 4)
        ac_change9 = round(unpacked_data[394], 4)
        ac_change10 = round(unpacked_data[395], 4)
        ac_current_change1 = round(unpacked_data[396], 4)
        ac_current_change2 = round(unpacked_data[397], 4)
        ac_current_change3 = round(unpacked_data[398], 4)
        ac_current_change4 = round(unpacked_data[399], 4)
        ac_current_change5 = round(unpacked_data[400], 4)
        ac_current_change6 = round(unpacked_data[401], 4)
        ac_current_change7 = round(unpacked_data[402], 4)
        ac_current_change8 = round(unpacked_data[403], 4)
        ac_current_change9 = round(unpacked_data[404], 4)
        ac_current_change10 = round(unpacked_data[405], 4)
        ad = round(unpacked_data[406], 4)
        ad_change1 = round(unpacked_data[407], 4)
        ad_change2 = round(unpacked_data[408], 4)
        ad_change3 = round(unpacked_data[409], 4)
        ad_change4 = round(unpacked_data[410], 4)
        ad_change5 = round(unpacked_data[411], 4)
        ad_change6 = round(unpacked_data[412], 4)
        ad_change7 = round(unpacked_data[413], 4)
        ad_change8 = round(unpacked_data[414], 4)
        ad_change9 = round(unpacked_data[415], 4)
        ad_change10 = round(unpacked_data[416], 4)
        ad_current_change1 = round(unpacked_data[417], 4)
        ad_current_change2 = round(unpacked_data[418], 4)
        ad_current_change3 = round(unpacked_data[419], 4)
        ad_current_change4 = round(unpacked_data[420], 4)
        ad_current_change5 = round(unpacked_data[421], 4)
        ad_current_change6 = round(unpacked_data[422], 4)
        ad_current_change7 = round(unpacked_data[423], 4)
        ad_current_change8 = round(unpacked_data[424], 4)
        ad_current_change9 = round(unpacked_data[425], 4)
        ad_current_change10 = round(unpacked_data[426], 4)
        adxWilder = round(unpacked_data[427], 4)
        adxWilder_DI_plus = round(unpacked_data[428], 4)
        adxWilder_DI_minus = round(unpacked_data[429], 4)
        adxWilder_change1 = round(unpacked_data[430], 4)
        adxWilder_change2 = round(unpacked_data[431], 4)
        adxWilder_change3 = round(unpacked_data[432], 4)
        adxWilder_change4 = round(unpacked_data[433], 4)
        adxWilder_change5 = round(unpacked_data[434], 4)
        adxWilder_change6 = round(unpacked_data[435], 4)
        adxWilder_change7 = round(unpacked_data[436], 4)
        adxWilder_change8 = round(unpacked_data[437], 4)
        adxWilder_change9 = round(unpacked_data[438], 4)
        adxWilder_change10 = round(unpacked_data[439], 4)
        adxWilder_current_change1 = round(unpacked_data[440], 4)
        adxWilder_current_change2 = round(unpacked_data[441], 4)
        adxWilder_current_change3 = round(unpacked_data[442], 4)
        adxWilder_current_change4 = round(unpacked_data[443], 4)
        adxWilder_current_change5 = round(unpacked_data[444], 4)
        adxWilder_current_change6 = round(unpacked_data[445], 4)
        adxWilder_current_change7 = round(unpacked_data[446], 4)
        adxWilder_current_change8 = round(unpacked_data[447], 4)
        adxWilder_current_change9 = round(unpacked_data[448], 4)
        adxWilder_current_change10 = round(unpacked_data[449], 4)
        jaws = round(unpacked_data[450], 4)
        teeth = round(unpacked_data[451], 4)
        lips = round(unpacked_data[452], 4)
        lips_change1 = round(unpacked_data[453], 4)
        lips_change2 = round(unpacked_data[454], 4)
        lips_change3 = round(unpacked_data[455], 4)
        lips_change4 = round(unpacked_data[456], 4)
        lips_change5 = round(unpacked_data[457], 4)
        lips_change6 = round(unpacked_data[458], 4)
        lips_change7 = round(unpacked_data[459], 4)
        lips_change8 = round(unpacked_data[460], 4)
        lips_change9 = round(unpacked_data[461], 4)
        lips_change10 = round(unpacked_data[462], 4)
        lips_current_change1 = round(unpacked_data[463], 4)
        lips_current_change2 = round(unpacked_data[464], 4)
        lips_current_change3 = round(unpacked_data[465], 4)
        lips_current_change4 = round(unpacked_data[466], 4)
        lips_current_change5 = round(unpacked_data[467], 4)
        lips_current_change6 = round(unpacked_data[468], 4)
        lips_current_change7 = round(unpacked_data[469], 4)
        lips_current_change8 = round(unpacked_data[470], 4)
        lips_current_change9 = round(unpacked_data[471], 4)
        lips_current_change10 = round(unpacked_data[472], 4)
        ama = round(unpacked_data[473], 4)
        ama_change1 = round(unpacked_data[474], 4)
        ama_change2 = round(unpacked_data[475], 4)
        ama_change3 = round(unpacked_data[476], 4)
        ama_change4 = round(unpacked_data[477], 4)
        ama_change5 = round(unpacked_data[478], 4)
        ama_change6 = round(unpacked_data[479], 4)
        ama_change7 = round(unpacked_data[480], 4)
        ama_change8 = round(unpacked_data[481], 4)
        ama_change9 = round(unpacked_data[482], 4)
        ama_change10 = round(unpacked_data[483], 4)
        ama_current_change1 = round(unpacked_data[484], 4)
        ama_current_change2 = round(unpacked_data[485], 4)
        ama_current_change3 = round(unpacked_data[486], 4)
        ama_current_change4 = round(unpacked_data[487], 4)
        ama_current_change5 = round(unpacked_data[488], 4)
        ama_current_change6 = round(unpacked_data[489], 4)
        ama_current_change7 = round(unpacked_data[490], 4)
        ama_current_change8 = round(unpacked_data[491], 4)
        ama_current_change9 = round(unpacked_data[492], 4)
        ama_current_change10 = round(unpacked_data[493], 4)
        ao_value = round(unpacked_data[494], 4)
        ao_color = round(unpacked_data[495], 4)
        ao_change1 = round(unpacked_data[496], 4)
        ao_change2 = round(unpacked_data[497], 4)
        ao_change3 = round(unpacked_data[498], 4)
        ao_change4 = round(unpacked_data[499], 4)
        ao_change5 = round(unpacked_data[500], 4)
        ao_change6 = round(unpacked_data[501], 4)
        ao_change7 = round(unpacked_data[502], 4)
        ao_change8 = round(unpacked_data[503], 4)
        ao_change9 = round(unpacked_data[504], 4)
        ao_change10 = round(unpacked_data[505], 4)
        ao_current_change1 = round(unpacked_data[506], 4)
        ao_current_change2 = round(unpacked_data[507], 4)
        ao_current_change3 = round(unpacked_data[508], 4)
        ao_current_change4 = round(unpacked_data[509], 4)
        ao_current_change5 = round(unpacked_data[510], 4)
        ao_current_change6 = round(unpacked_data[511], 4)
        ao_current_change7 = round(unpacked_data[512], 4)
        ao_current_change8 = round(unpacked_data[513], 4)
        ao_current_change9 = round(unpacked_data[514], 4)
        ao_current_change10 = round(unpacked_data[515], 4)
        bearsPower = round(unpacked_data[516], 4)
        bears_change1 = round(unpacked_data[517], 4)
        bears_change2 = round(unpacked_data[518], 4)
        bears_change3 = round(unpacked_data[519], 4)
        bears_change4 = round(unpacked_data[520], 4)
        bears_change5 = round(unpacked_data[521], 4)
        bears_change6 = round(unpacked_data[522], 4)
        bears_change7 = round(unpacked_data[523], 4)
        bears_change8 = round(unpacked_data[524], 4)
        bears_change9 = round(unpacked_data[525], 4)
        bears_change10 = round(unpacked_data[526], 4)
        bears_current_change1 = round(unpacked_data[527], 4)
        bears_current_change2 = round(unpacked_data[528], 4)
        bears_current_change3 = round(unpacked_data[529], 4)
        bears_current_change4 = round(unpacked_data[530], 4)
        bears_current_change5 = round(unpacked_data[531], 4)
        bears_current_change6 = round(unpacked_data[532], 4)
        bears_current_change7 = round(unpacked_data[533], 4)
        bears_current_change8 = round(unpacked_data[534], 4)
        bears_current_change9 = round(unpacked_data[535], 4)
        bears_current_change10 = round(unpacked_data[536], 4)
        bullsPower = round(unpacked_data[537], 4)
        bulls_change1 = round(unpacked_data[538], 4)
        bulls_change2 = round(unpacked_data[539], 4)
        bulls_change3 = round(unpacked_data[540], 4)
        bulls_change4 = round(unpacked_data[541], 4)
        bulls_change5 = round(unpacked_data[542], 4)
        bulls_change6 = round(unpacked_data[543], 4)
        bulls_change7 = round(unpacked_data[544], 4)
        bulls_change8 = round(unpacked_data[545], 4)
        bulls_change9 = round(unpacked_data[546], 4)
        bulls_change10 = round(unpacked_data[547], 4)
        bulls_current_change1 = round(unpacked_data[548], 4)
        bulls_current_change2 = round(unpacked_data[549], 4)
        bulls_current_change3 = round(unpacked_data[550], 4)
        bulls_current_change4 = round(unpacked_data[551], 4)
        bulls_current_change5 = round(unpacked_data[552], 4)
        bulls_current_change6 = round(unpacked_data[553], 4)
        bulls_current_change7 = round(unpacked_data[554], 4)
        bulls_current_change8 = round(unpacked_data[555], 4)
        bulls_current_change9 = round(unpacked_data[556], 4)
        bulls_current_change10 = round(unpacked_data[557], 4)
        chaikin = round(unpacked_data[558], 4)
        chaikin_change1 = round(unpacked_data[559], 4)
        chaikin_change2 = round(unpacked_data[560], 4)
        chaikin_change3 = round(unpacked_data[561], 4)
        chaikin_change4 = round(unpacked_data[562], 4)
        chaikin_change5 = round(unpacked_data[563], 4)
        chaikin_change6 = round(unpacked_data[564], 4)
        chaikin_change7 = round(unpacked_data[565], 4)
        chaikin_change8 = round(unpacked_data[566], 4)
        chaikin_change9 = round(unpacked_data[567], 4)
        chaikin_change10 = round(unpacked_data[568], 4)
        chaikin_current_change1 = round(unpacked_data[569], 4)
        chaikin_current_change2 = round(unpacked_data[570], 4)
        chaikin_current_change3 = round(unpacked_data[571], 4)
        chaikin_current_change4 = round(unpacked_data[572], 4)
        chaikin_current_change5 = round(unpacked_data[573], 4)
        chaikin_current_change6 = round(unpacked_data[574], 4)
        chaikin_current_change7 = round(unpacked_data[575], 4)
        chaikin_current_change8 = round(unpacked_data[576], 4)
        chaikin_current_change9 = round(unpacked_data[577], 4)
        chaikin_current_change10 = round(unpacked_data[578], 4)
        dema = round(unpacked_data[579], 4)
        dema_change1 = round(unpacked_data[580], 4)
        dema_change2 = round(unpacked_data[581], 4)
        dema_change3 = round(unpacked_data[582], 4)
        dema_change4 = round(unpacked_data[583], 4)
        dema_change5 = round(unpacked_data[584], 4)
        dema_change6 = round(unpacked_data[585], 4)
        dema_change7 = round(unpacked_data[586], 4)
        dema_change8 = round(unpacked_data[587], 4)
        dema_change9 = round(unpacked_data[588], 4)
        dema_change10 = round(unpacked_data[589], 4)
        dema_current_change1 = round(unpacked_data[590], 4)
        dema_current_change2 = round(unpacked_data[591], 4)
        dema_current_change3 = round(unpacked_data[592], 4)
        dema_current_change4 = round(unpacked_data[593], 4)
        dema_current_change5 = round(unpacked_data[594], 4)
        dema_current_change6 = round(unpacked_data[595], 4)
        dema_current_change7 = round(unpacked_data[596], 4)
        dema_current_change8 = round(unpacked_data[597], 4)
        dema_current_change9 = round(unpacked_data[598], 4)
        dema_current_change10 = round(unpacked_data[599], 4)
        deMarker = round(unpacked_data[600], 4)
        deMarker_change1 = round(unpacked_data[601], 4)
        deMarker_change2 = round(unpacked_data[602], 4)
        deMarker_change3 = round(unpacked_data[603], 4)
        deMarker_change4 = round(unpacked_data[604], 4)
        deMarker_change5 = round(unpacked_data[605], 4)
        deMarker_change6 = round(unpacked_data[606], 4)
        deMarker_change7 = round(unpacked_data[607], 4)
        deMarker_change8 = round(unpacked_data[608], 4)
        deMarker_change9 = round(unpacked_data[609], 4)
        deMarker_change10 = round(unpacked_data[610], 4)
        deMarker_current_change1 = round(unpacked_data[611], 4)
        deMarker_current_change2 = round(unpacked_data[612], 4)
        deMarker_current_change3 = round(unpacked_data[613], 4)
        deMarker_current_change4 = round(unpacked_data[614], 4)
        deMarker_current_change5 = round(unpacked_data[615], 4)
        deMarker_current_change6 = round(unpacked_data[616], 4)
        deMarker_current_change7 = round(unpacked_data[617], 4)
        deMarker_current_change8 = round(unpacked_data[618], 4)
        deMarker_current_change9 = round(unpacked_data[619], 4)
        deMarker_current_change10 = round(unpacked_data[620], 4)
        envelopes_upper_value = round(unpacked_data[621], 4)
        envelopes_lower_value = round(unpacked_data[622], 4)
        force = round(unpacked_data[623], 4)
        force_change1 = round(unpacked_data[624], 4)
        force_change2 = round(unpacked_data[625], 4)
        force_change3 = round(unpacked_data[626], 4)
        force_change4 = round(unpacked_data[627], 4)
        force_change5 = round(unpacked_data[628], 4)
        force_change6 = round(unpacked_data[629], 4)
        force_change7 = round(unpacked_data[630], 4)
        force_change8 = round(unpacked_data[631], 4)
        force_change9 = round(unpacked_data[632], 4)
        force_change10 = round(unpacked_data[633], 4)
        force_current_change1 = round(unpacked_data[634], 4)
        force_current_change2 = round(unpacked_data[635], 4)
        force_current_change3 = round(unpacked_data[636], 4)
        force_current_change4 = round(unpacked_data[637], 4)
        force_current_change5 = round(unpacked_data[638], 4)
        force_current_change6 = round(unpacked_data[639], 4)
        force_current_change7 = round(unpacked_data[640], 4)
        force_current_change8 = round(unpacked_data[641], 4)
        force_current_change9 = round(unpacked_data[642], 4)
        force_current_change10 = round(unpacked_data[643], 4)
        fractals_up_arrow = round(unpacked_data[644], 4)
        fractals_down_arrow = round(unpacked_data[645], 4)
        frAMA = round(unpacked_data[646], 4)
        frAMA_change1 = round(unpacked_data[647], 4)
        frAMA_change2 = round(unpacked_data[648], 4)
        frAMA_change3 = round(unpacked_data[649], 4)
        frAMA_change4 = round(unpacked_data[650], 4)
        frAMA_change5 = round(unpacked_data[651], 4)
        frAMA_change6 = round(unpacked_data[652], 4)
        frAMA_change7 = round(unpacked_data[653], 4)
        frAMA_change8 = round(unpacked_data[654], 4)
        frAMA_change9 = round(unpacked_data[655], 4)
        frAMA_change10 = round(unpacked_data[656], 4)
        frAMA_current_change1 = round(unpacked_data[657], 4)
        frAMA_current_change2 = round(unpacked_data[658], 4)
        frAMA_current_change3 = round(unpacked_data[659], 4)
        frAMA_current_change4 = round(unpacked_data[660], 4)
        frAMA_current_change5 = round(unpacked_data[661], 4)
        frAMA_current_change6 = round(unpacked_data[662], 4)
        frAMA_current_change7 = round(unpacked_data[663], 4)
        frAMA_current_change8 = round(unpacked_data[664], 4)
        frAMA_current_change9 = round(unpacked_data[665], 4)
        frAMA_current_change10 = round(unpacked_data[666], 4)
        gator_ups = round(unpacked_data[667], 4)
        gator_up_color = round(unpacked_data[668], 4)
        gator_downs = round(unpacked_data[669], 4)
        gator_downs_color = round(unpacked_data[670], 4)
        tenkan_sen = round(unpacked_data[671], 4)
        kijun_sen = round(unpacked_data[672], 4)
        senkou_span_A = round(unpacked_data[673], 4)
        senkou_span_B = round(unpacked_data[674], 4)
        chinkou_span = round(unpacked_data[675], 4)
        bwmfi_value = round(unpacked_data[676], 4)
        bwmfi_color = round(unpacked_data[677], 4)
        bwmfi_change1 = round(unpacked_data[678], 4)
        bwmfi_change2 = round(unpacked_data[679], 4)
        bwmfi_change3 = round(unpacked_data[680], 4)
        bwmfi_change4 = round(unpacked_data[681], 4)
        bwmfi_change5 = round(unpacked_data[682], 4)
        bwmfi_change6 = round(unpacked_data[683], 4)
        bwmfi_change7 = round(unpacked_data[684], 4)
        bwmfi_change8 = round(unpacked_data[685], 4)
        bwmfi_change9 = round(unpacked_data[686], 4)
        bwmfi_change10 = round(unpacked_data[687], 4)
        bwmfi_current_change1 = round(unpacked_data[688], 4)
        bwmfi_current_change2 = round(unpacked_data[689], 4)
        bwmfi_current_change3 = round(unpacked_data[690], 4)
        bwmfi_current_change4 = round(unpacked_data[691], 4)
        bwmfi_current_change5 = round(unpacked_data[692], 4)
        bwmfi_current_change6 = round(unpacked_data[693], 4)
        bwmfi_current_change7 = round(unpacked_data[694], 4)
        bwmfi_current_change8 = round(unpacked_data[695], 4)
        bwmfi_current_change9 = round(unpacked_data[696], 4)
        bwmfi_current_change10 = round(unpacked_data[697], 4)
        momentum = round(unpacked_data[698], 4)
        momentum_change1 = round(unpacked_data[699], 4)
        momentum_change2 = round(unpacked_data[700], 4)
        momentum_change3 = round(unpacked_data[701], 4)
        momentum_change4 = round(unpacked_data[702], 4)
        momentum_change5 = round(unpacked_data[703], 4)
        momentum_change6 = round(unpacked_data[704], 4)
        momentum_change7 = round(unpacked_data[705], 4)
        momentum_change8 = round(unpacked_data[706], 4)
        momentum_change9 = round(unpacked_data[707], 4)
        momentum_change10 = round(unpacked_data[708], 4)
        momentum_current_change1 = round(unpacked_data[709], 4)
        momentum_current_change2 = round(unpacked_data[710], 4)
        momentum_current_change3 = round(unpacked_data[711], 4)
        momentum_current_change4 = round(unpacked_data[712], 4)
        momentum_current_change5 = round(unpacked_data[713], 4)
        momentum_current_change6 = round(unpacked_data[714], 4)
        momentum_current_change7 = round(unpacked_data[715], 4)
        momentum_current_change8 = round(unpacked_data[716], 4)
        momentum_current_change9 = round(unpacked_data[717], 4)
        momentum_current_change10 = round(unpacked_data[718], 4)
        mfi = round(unpacked_data[719], 4)
        mfi_change1 = round(unpacked_data[720], 4)
        mfi_change2 = round(unpacked_data[721], 4)
        mfi_change3 = round(unpacked_data[722], 4)
        mfi_change4 = round(unpacked_data[723], 4)
        mfi_change5 = round(unpacked_data[724], 4)
        mfi_change6 = round(unpacked_data[725], 4)
        mfi_change7 = round(unpacked_data[726], 4)
        mfi_change8 = round(unpacked_data[727], 4)
        mfi_change9 = round(unpacked_data[728], 4)
        mfi_change10 = round(unpacked_data[729], 4)
        mfi_current_change1 = round(unpacked_data[730], 4)
        mfi_current_change2 = round(unpacked_data[731], 4)
        mfi_current_change3 = round(unpacked_data[732], 4)
        mfi_current_change4 = round(unpacked_data[733], 4)
        mfi_current_change5 = round(unpacked_data[734], 4)
        mfi_current_change6 = round(unpacked_data[735], 4)
        mfi_current_change7 = round(unpacked_data[736], 4)
        mfi_current_change8 = round(unpacked_data[737], 4)
        mfi_current_change9 = round(unpacked_data[738], 4)
        mfi_current_change10 = round(unpacked_data[739], 4)
        osMA = round(unpacked_data[740], 4)
        osMA_change1 = round(unpacked_data[741], 4)
        osMA_change2 = round(unpacked_data[742], 4)
        osMA_change3 = round(unpacked_data[743], 4)
        osMA_change4 = round(unpacked_data[744], 4)
        osMA_change5 = round(unpacked_data[745], 4)
        osMA_change6 = round(unpacked_data[746], 4)
        osMA_change7 = round(unpacked_data[747], 4)
        osMA_change8 = round(unpacked_data[748], 4)
        osMA_change9 = round(unpacked_data[749], 4)
        osMA_change10 = round(unpacked_data[750], 4)
        osMA_current_change1 = round(unpacked_data[751], 4)
        osMA_current_change2 = round(unpacked_data[752], 4)
        osMA_current_change3 = round(unpacked_data[753], 4)
        osMA_current_change4 = round(unpacked_data[754], 4)
        osMA_current_change5 = round(unpacked_data[755], 4)
        osMA_current_change6 = round(unpacked_data[756], 4)
        osMA_current_change7 = round(unpacked_data[757], 4)
        osMA_current_change8 = round(unpacked_data[758], 4)
        osMA_current_change9 = round(unpacked_data[759], 4)
        osMA_current_change10 = round(unpacked_data[760], 4)
        obv = round(unpacked_data[761], 4)
        obv_change1 = round(unpacked_data[762], 4)
        obv_change2 = round(unpacked_data[763], 4)
        obv_change3 = round(unpacked_data[764], 4)
        obv_change4 = round(unpacked_data[765], 4)
        obv_change5 = round(unpacked_data[766], 4)
        obv_change6 = round(unpacked_data[767], 4)
        obv_change7 = round(unpacked_data[768], 4)
        obv_change8 = round(unpacked_data[769], 4)
        obv_change9 = round(unpacked_data[770], 4)
        obv_change10 = round(unpacked_data[771], 4)
        obv_current_change1 = round(unpacked_data[772], 4)
        obv_current_change2 = round(unpacked_data[773], 4)
        obv_current_change3 = round(unpacked_data[774], 4)
        obv_current_change4 = round(unpacked_data[775], 4)
        obv_current_change5 = round(unpacked_data[776], 4)
        obv_current_change6 = round(unpacked_data[777], 4)
        obv_current_change7 = round(unpacked_data[778], 4)
        obv_current_change8 = round(unpacked_data[779], 4)
        obv_current_change9 = round(unpacked_data[780], 4)
        obv_current_change10 = round(unpacked_data[781], 4)
        rvi = round(unpacked_data[782], 4)
        rvi_signal = round(unpacked_data[783], 4)
        rvi_change1 = round(unpacked_data[784], 4)
        rvi_change2 = round(unpacked_data[785], 4)
        rvi_change3 = round(unpacked_data[786], 4)
        rvi_change4 = round(unpacked_data[787], 4)
        rvi_change5 = round(unpacked_data[788], 4)
        rvi_change6 = round(unpacked_data[789], 4)
        rvi_change7 = round(unpacked_data[790], 4)
        rvi_change8 = round(unpacked_data[791], 4)
        rvi_change9 = round(unpacked_data[792], 4)
        rvi_change10 = round(unpacked_data[793], 4)
        rvi_current_change1 = round(unpacked_data[794], 4)
        rvi_current_change2 = round(unpacked_data[795], 4)
        rvi_current_change3 = round(unpacked_data[796], 4)
        rvi_current_change4 = round(unpacked_data[797], 4)
        rvi_current_change5 = round(unpacked_data[798], 4)
        rvi_current_change6 = round(unpacked_data[799], 4)
        rvi_current_change7 = round(unpacked_data[800], 4)
        rvi_current_change8 = round(unpacked_data[801], 4)
        rvi_current_change9 = round(unpacked_data[802], 4)
        rvi_current_change10 = round(unpacked_data[803], 4)
        stdDev = round(unpacked_data[804], 4)
        stdDev_change1 = round(unpacked_data[805], 4)
        stdDev_change2 = round(unpacked_data[806], 4)
        stdDev_change3 = round(unpacked_data[807], 4)
        stdDev_change4 = round(unpacked_data[808], 4)
        stdDev_change5 = round(unpacked_data[809], 4)
        stdDev_change6 = round(unpacked_data[810], 4)
        stdDev_change7 = round(unpacked_data[811], 4)
        stdDev_change8 = round(unpacked_data[812], 4)
        stdDev_change9 = round(unpacked_data[813], 4)
        stdDev_change10 = round(unpacked_data[814], 4)
        stdDev_current_change1 = round(unpacked_data[815], 4)
        stdDev_current_change2 = round(unpacked_data[816], 4)
        stdDev_current_change3 = round(unpacked_data[817], 4)
        stdDev_current_change4 = round(unpacked_data[818], 4)
        stdDev_current_change5 = round(unpacked_data[819], 4)
        stdDev_current_change6 = round(unpacked_data[820], 4)
        stdDev_current_change7 = round(unpacked_data[821], 4)
        stdDev_current_change8 = round(unpacked_data[822], 4)
        stdDev_current_change9 = round(unpacked_data[823], 4)
        stdDev_current_change10 = round(unpacked_data[824], 4)
        tema = round(unpacked_data[825], 4)
        tema_change1 = round(unpacked_data[826], 4)
        tema_change2 = round(unpacked_data[827], 4)
        tema_change3 = round(unpacked_data[828], 4)
        tema_change4 = round(unpacked_data[829], 4)
        tema_change5 = round(unpacked_data[830], 4)
        tema_change6 = round(unpacked_data[831], 4)
        tema_change7 = round(unpacked_data[832], 4)
        tema_change8 = round(unpacked_data[833], 4)
        tema_change9 = round(unpacked_data[834], 4)
        tema_change10 = round(unpacked_data[835], 4)
        tema_current_change1 = round(unpacked_data[836], 4)
        tema_current_change2 = round(unpacked_data[837], 4)
        tema_current_change3 = round(unpacked_data[838], 4)
        tema_current_change4 = round(unpacked_data[839], 4)
        tema_current_change5 = round(unpacked_data[840], 4)
        tema_current_change6 = round(unpacked_data[841], 4)
        tema_current_change7 = round(unpacked_data[842], 4)
        tema_current_change8 = round(unpacked_data[843], 4)
        tema_current_change9 = round(unpacked_data[844], 4)
        tema_current_change10 = round(unpacked_data[845], 4)
        triX = round(unpacked_data[846], 4)
        triX_change1 = round(unpacked_data[847], 4)
        triX_change2 = round(unpacked_data[848], 4)
        triX_change3 = round(unpacked_data[849], 4)
        triX_change4 = round(unpacked_data[850], 4)
        triX_change5 = round(unpacked_data[851], 4)
        triX_change6 = round(unpacked_data[852], 4)
        triX_change7 = round(unpacked_data[853], 4)
        triX_change8 = round(unpacked_data[854], 4)
        triX_change9 = round(unpacked_data[855], 4)
        triX_change10 = round(unpacked_data[856], 4)
        triX_current_change1 = round(unpacked_data[857], 4)
        triX_current_change2 = round(unpacked_data[858], 4)
        triX_current_change3 = round(unpacked_data[859], 4)
        triX_current_change4 = round(unpacked_data[860], 4)
        triX_current_change5 = round(unpacked_data[861], 4)
        triX_current_change6 = round(unpacked_data[862], 4)
        triX_current_change7 = round(unpacked_data[863], 4)
        triX_current_change8 = round(unpacked_data[864], 4)
        triX_current_change9 = round(unpacked_data[865], 4)
        triX_current_change10 = round(unpacked_data[866], 4)
        wpr = round(unpacked_data[867], 4)
        wpr_change1 = round(unpacked_data[868], 4)
        wpr_change2 = round(unpacked_data[869], 4)
        wpr_change3 = round(unpacked_data[870], 4)
        wpr_change4 = round(unpacked_data[871], 4)
        wpr_change5 = round(unpacked_data[872], 4)
        wpr_change6 = round(unpacked_data[873], 4)
        wpr_change7 = round(unpacked_data[874], 4)
        wpr_change8 = round(unpacked_data[875], 4)
        wpr_change9 = round(unpacked_data[876], 4)
        wpr_change10 = round(unpacked_data[877], 4)
        wpr_current_change1 = round(unpacked_data[878], 4)
        wpr_current_change2 = round(unpacked_data[879], 4)
        wpr_current_change3 = round(unpacked_data[880], 4)
        wpr_current_change4 = round(unpacked_data[881], 4)
        wpr_current_change5 = round(unpacked_data[882], 4)
        wpr_current_change6 = round(unpacked_data[883], 4)
        wpr_current_change7 = round(unpacked_data[884], 4)
        wpr_current_change8 = round(unpacked_data[885], 4)
        wpr_current_change9 = round(unpacked_data[886], 4)
        wpr_current_change10 = round(unpacked_data[887], 4)
        vidya = round(unpacked_data[888], 4)
        vidya_change1 = round(unpacked_data[889], 4)
        vidya_change2 = round(unpacked_data[890], 4)
        vidya_change3 = round(unpacked_data[891], 4)
        vidya_change4 = round(unpacked_data[892], 4)
        vidya_change5 = round(unpacked_data[893], 4)
        vidya_change6 = round(unpacked_data[894], 4)
        vidya_change7 = round(unpacked_data[895], 4)
        vidya_change8 = round(unpacked_data[896], 4)
        vidya_change9 = round(unpacked_data[897], 4)
        vidya_change10 = round(unpacked_data[898], 4)
        vidya_current_change1 = round(unpacked_data[899], 4)
        vidya_current_change2 = round(unpacked_data[900], 4)
        vidya_current_change3 = round(unpacked_data[901], 4)
        vidya_current_change4 = round(unpacked_data[902], 4)
        vidya_current_change5 = round(unpacked_data[903], 4)
        vidya_current_change6 = round(unpacked_data[904], 4)
        vidya_current_change7 = round(unpacked_data[905], 4)
        vidya_current_change8 = round(unpacked_data[906], 4)
        vidya_current_change9 = round(unpacked_data[907], 4)
        vidya_current_change10 = round(unpacked_data[908], 4)
        atr_5_10_type = int(unpacked_data[909])
        macd_type = int(unpacked_data[910])
        sma_5_10_type = int(unpacked_data[911])
        ema_5_10_type = int(unpacked_data[912])
        smma_5_10_type = int(unpacked_data[913])
        lwma_5_10_type = int(unpacked_data[914])
        rsi_5_14_type = int(unpacked_data[915])
        sar_type = int(unpacked_data[916])
        adx_type = int(unpacked_data[917])
        cci_type = int(unpacked_data[918])
        stoch_type = int(unpacked_data[919])
        boll_type = int(unpacked_data[920])
        ac_type = int(unpacked_data[921])
        ad_type = int(unpacked_data[922])
        adxWilder_type = int(unpacked_data[923])
        alligator_type = int(unpacked_data[924])
        ama_type = int(unpacked_data[925])
        ao_type = int(unpacked_data[926])
        bearsPower_type = int(unpacked_data[927])
        bullsPower_type = int(unpacked_data[928])
        chaikin_type = int(unpacked_data[929])
        dema_type = int(unpacked_data[930])
        deMarker_type = int(unpacked_data[931])
        envelopes_type = int(unpacked_data[932])
        force_type = int(unpacked_data[933])
        fractals_type = int(unpacked_data[934])
        frAMA_type = int(unpacked_data[935])
        gator_type = int(unpacked_data[936])
        ichimoku_type = int(unpacked_data[937])
        bwmfi_type = int(unpacked_data[938])
        momentum_type = int(unpacked_data[939])
        mfi_type = int(unpacked_data[940])
        osMA_type = int(unpacked_data[941])
        obv_type = int(unpacked_data[942])
        rvi_type = int(unpacked_data[943])
        stdDev_type = int(unpacked_data[944])
        tema_type = int(unpacked_data[945])
        triX_type = int(unpacked_data[946])
        wpr_type = int(unpacked_data[947])
        vidya_type = int(unpacked_data[948])
        atr5_changeValue1 = round(unpacked_data[949], 4)
        atr5_changeValue2 = round(unpacked_data[950], 4)
        atr5_changeValue3 = round(unpacked_data[951], 4)
        atr5_changeValue4 = round(unpacked_data[952], 4)
        atr5_changeValue5 = round(unpacked_data[953], 4)
        atr5_changeValue6 = round(unpacked_data[954], 4)
        atr5_changeValue7 = round(unpacked_data[955], 4)
        atr5_changeValue8 = round(unpacked_data[956], 4)
        atr5_changeValue9 = round(unpacked_data[957], 4)
        atr5_changeValue10 = round(unpacked_data[958], 4)
        atr10_changeValue1 = round(unpacked_data[959], 4)
        atr10_changeValue2 = round(unpacked_data[960], 4)
        atr10_changeValue3 = round(unpacked_data[961], 4)
        atr10_changeValue4 = round(unpacked_data[962], 4)
        atr10_changeValue5 = round(unpacked_data[963], 4)
        atr10_changeValue6 = round(unpacked_data[964], 4)
        atr10_changeValue7 = round(unpacked_data[965], 4)
        atr10_changeValue8 = round(unpacked_data[966], 4)
        atr10_changeValue9 = round(unpacked_data[967], 4)
        atr10_changeValue10 = round(unpacked_data[968], 4)
        macd_changeValue1 = round(unpacked_data[969], 4)
        macd_changeValue2 = round(unpacked_data[970], 4)
        macd_changeValue3 = round(unpacked_data[971], 4)
        macd_changeValue4 = round(unpacked_data[972], 4)
        macd_changeValue5 = round(unpacked_data[973], 4)
        macd_changeValue6 = round(unpacked_data[974], 4)
        macd_changeValue7 = round(unpacked_data[975], 4)
        macd_changeValue8 = round(unpacked_data[976], 4)
        macd_changeValue9 = round(unpacked_data[977], 4)
        macd_changeValue10 = round(unpacked_data[978], 4)
        sma5_changeValue1 = round(unpacked_data[979], 4)
        sma5_changeValue2 = round(unpacked_data[980], 4)
        sma5_changeValue3 = round(unpacked_data[981], 4)
        sma5_changeValue4 = round(unpacked_data[982], 4)
        sma5_changeValue5 = round(unpacked_data[983], 4)
        sma5_changeValue6 = round(unpacked_data[984], 4)
        sma5_changeValue7 = round(unpacked_data[985], 4)
        sma5_changeValue8 = round(unpacked_data[986], 4)
        sma5_changeValue9 = round(unpacked_data[987], 4)
        sma5_changeValue10 = round(unpacked_data[988], 4)
        sma10_changeValue1 = round(unpacked_data[989], 4)
        sma10_changeValue2 = round(unpacked_data[990], 4)
        sma10_changeValue3 = round(unpacked_data[991], 4)
        sma10_changeValue4 = round(unpacked_data[992], 4)
        sma10_changeValue5 = round(unpacked_data[993], 4)
        sma10_changeValue6 = round(unpacked_data[994], 4)
        sma10_changeValue7 = round(unpacked_data[995], 4)
        sma10_changeValue8 = round(unpacked_data[996], 4)
        sma10_changeValue9 = round(unpacked_data[997], 4)
        sma10_changeValue10 = round(unpacked_data[998], 4)
        rsi5_changeValue1 = round(unpacked_data[999], 4)
        rsi5_changeValue2 = round(unpacked_data[1000], 4)
        rsi5_changeValue3 = round(unpacked_data[1001], 4)
        rsi5_changeValue4 = round(unpacked_data[1002], 4)
        rsi5_changeValue5 = round(unpacked_data[1003], 4)
        rsi5_changeValue6 = round(unpacked_data[1004], 4)
        rsi5_changeValue7 = round(unpacked_data[1005], 4)
        rsi5_changeValue8 = round(unpacked_data[1006], 4)
        rsi5_changeValue9 = round(unpacked_data[1007], 4)
        rsi5_changeValue10 = round(unpacked_data[1008], 4)
        rsi14_changeValue1 = round(unpacked_data[1009], 4)
        rsi14_changeValue2 = round(unpacked_data[1010], 4)
        rsi14_changeValue3 = round(unpacked_data[1011], 4)
        rsi14_changeValue4 = round(unpacked_data[1012], 4)
        rsi14_changeValue5 = round(unpacked_data[1013], 4)
        rsi14_changeValue6 = round(unpacked_data[1014], 4)
        rsi14_changeValue7 = round(unpacked_data[1015], 4)
        rsi14_changeValue8 = round(unpacked_data[1016], 4)
        rsi14_changeValue9 = round(unpacked_data[1017], 4)
        rsi14_changeValue10 = round(unpacked_data[1018], 4)
        sar_changeValue1 = round(unpacked_data[1019], 4)
        sar_changeValue2 = round(unpacked_data[1020], 4)
        sar_changeValue3 = round(unpacked_data[1021], 4)
        sar_changeValue4 = round(unpacked_data[1022], 4)
        sar_changeValue5 = round(unpacked_data[1023], 4)
        sar_changeValue6 = round(unpacked_data[1024], 4)
        sar_changeValue7 = round(unpacked_data[1025], 4)
        sar_changeValue8 = round(unpacked_data[1026], 4)
        sar_changeValue9 = round(unpacked_data[1027], 4)
        sar_changeValue10 = round(unpacked_data[1028], 4)
        adx_changeValue1 = round(unpacked_data[1029], 4)
        adx_changeValue2 = round(unpacked_data[1030], 4)
        adx_changeValue3 = round(unpacked_data[1031], 4)
        adx_changeValue4 = round(unpacked_data[1032], 4)
        adx_changeValue5 = round(unpacked_data[1033], 4)
        adx_changeValue6 = round(unpacked_data[1034], 4)
        adx_changeValue7 = round(unpacked_data[1035], 4)
        adx_changeValue8 = round(unpacked_data[1036], 4)
        adx_changeValue9 = round(unpacked_data[1037], 4)
        adx_changeValue10 = round(unpacked_data[1038], 4)
        cci_changeValue1 = round(unpacked_data[1039], 4)
        cci_changeValue2 = round(unpacked_data[1040], 4)
        cci_changeValue3 = round(unpacked_data[1041], 4)
        cci_changeValue4 = round(unpacked_data[1042], 4)
        cci_changeValue5 = round(unpacked_data[1043], 4)
        cci_changeValue6 = round(unpacked_data[1044], 4)
        cci_changeValue7 = round(unpacked_data[1045], 4)
        cci_changeValue8 = round(unpacked_data[1046], 4)
        cci_changeValue9 = round(unpacked_data[1047], 4)
        cci_changeValue10 = round(unpacked_data[1048], 4)
        slowk_changeValue1 = round(unpacked_data[1049], 4)
        slowk_changeValue2 = round(unpacked_data[1050], 4)
        slowk_changeValue3 = round(unpacked_data[1051], 4)
        slowk_changeValue4 = round(unpacked_data[1052], 4)
        slowk_changeValue5 = round(unpacked_data[1053], 4)
        slowk_changeValue6 = round(unpacked_data[1054], 4)
        slowk_changeValue7 = round(unpacked_data[1055], 4)
        slowk_changeValue8 = round(unpacked_data[1056], 4)
        slowk_changeValue9 = round(unpacked_data[1057], 4)
        slowk_changeValue10 = round(unpacked_data[1058], 4)
        ac_changeValue1 = round(unpacked_data[1059], 4)
        ac_changeValue2 = round(unpacked_data[1060], 4)
        ac_changeValue3 = round(unpacked_data[1061], 4)
        ac_changeValue4 = round(unpacked_data[1062], 4)
        ac_changeValue5 = round(unpacked_data[1063], 4)
        ac_changeValue6 = round(unpacked_data[1064], 4)
        ac_changeValue7 = round(unpacked_data[1065], 4)
        ac_changeValue8 = round(unpacked_data[1066], 4)
        ac_changeValue9 = round(unpacked_data[1067], 4)
        ac_changeValue10 = round(unpacked_data[1068], 4)
        adxWilder_changeValue1 = round(unpacked_data[1069], 4)
        adxWilder_changeValue2 = round(unpacked_data[1070], 4)
        adxWilder_changeValue3 = round(unpacked_data[1071], 4)
        adxWilder_changeValue4 = round(unpacked_data[1072], 4)
        adxWilder_changeValue5 = round(unpacked_data[1073], 4)
        adxWilder_changeValue6 = round(unpacked_data[1074], 4)
        adxWilder_changeValue7 = round(unpacked_data[1075], 4)
        adxWilder_changeValue8 = round(unpacked_data[1076], 4)
        adxWilder_changeValue9 = round(unpacked_data[1077], 4)
        adxWilder_changeValue10 = round(unpacked_data[1078], 4)
        lips_changeValue1 = round(unpacked_data[1079], 4)
        lips_changeValue2 = round(unpacked_data[1080], 4)
        lips_changeValue3 = round(unpacked_data[1081], 4)
        lips_changeValue4 = round(unpacked_data[1082], 4)
        lips_changeValue5 = round(unpacked_data[1083], 4)
        lips_changeValue6 = round(unpacked_data[1084], 4)
        lips_changeValue7 = round(unpacked_data[1085], 4)
        lips_changeValue8 = round(unpacked_data[1086], 4)
        lips_changeValue9 = round(unpacked_data[1087], 4)
        lips_changeValue10 = round(unpacked_data[1088], 4)
        ama_changeValue1 = round(unpacked_data[1089], 4)
        ama_changeValue2 = round(unpacked_data[1090], 4)
        ama_changeValue3 = round(unpacked_data[1091], 4)
        ama_changeValue4 = round(unpacked_data[1092], 4)
        ama_changeValue5 = round(unpacked_data[1093], 4)
        ama_changeValue6 = round(unpacked_data[1094], 4)
        ama_changeValue7 = round(unpacked_data[1095], 4)
        ama_changeValue8 = round(unpacked_data[1096], 4)
        ama_changeValue9 = round(unpacked_data[1097], 4)
        ama_changeValue10 = round(unpacked_data[1098], 4)
        ao_changeValue1 = round(unpacked_data[1099], 4)
        ao_changeValue2 = round(unpacked_data[1100], 4)
        ao_changeValue3 = round(unpacked_data[1101], 4)
        ao_changeValue4 = round(unpacked_data[1102], 4)
        ao_changeValue5 = round(unpacked_data[1103], 4)
        ao_changeValue6 = round(unpacked_data[1104], 4)
        ao_changeValue7 = round(unpacked_data[1105], 4)
        ao_changeValue8 = round(unpacked_data[1106], 4)
        ao_changeValue9 = round(unpacked_data[1107], 4)
        ao_changeValue10 = round(unpacked_data[1108], 4)
        bears_changeValue1 = round(unpacked_data[1109], 4)
        bears_changeValue2 = round(unpacked_data[1110], 4)
        bears_changeValue3 = round(unpacked_data[1111], 4)
        bears_changeValue4 = round(unpacked_data[1112], 4)
        bears_changeValue5 = round(unpacked_data[1113], 4)
        bears_changeValue6 = round(unpacked_data[1114], 4)
        bears_changeValue7 = round(unpacked_data[1115], 4)
        bears_changeValue8 = round(unpacked_data[1116], 4)
        bears_changeValue9 = round(unpacked_data[1117], 4)
        bears_changeValue10 = round(unpacked_data[1118], 4)
        bulls_changeValue1 = round(unpacked_data[1119], 4)
        bulls_changeValue2 = round(unpacked_data[1120], 4)
        bulls_changeValue3 = round(unpacked_data[1121], 4)
        bulls_changeValue4 = round(unpacked_data[1122], 4)
        bulls_changeValue5 = round(unpacked_data[1123], 4)
        bulls_changeValue6 = round(unpacked_data[1124], 4)
        bulls_changeValue7 = round(unpacked_data[1125], 4)
        bulls_changeValue8 = round(unpacked_data[1126], 4)
        bulls_changeValue9 = round(unpacked_data[1127], 4)
        bulls_changeValue10 = round(unpacked_data[1128], 4)
        chaikin_changeValue1 = round(unpacked_data[1129], 4)
        chaikin_changeValue2 = round(unpacked_data[1130], 4)
        chaikin_changeValue3 = round(unpacked_data[1131], 4)
        chaikin_changeValue4 = round(unpacked_data[1132], 4)
        chaikin_changeValue5 = round(unpacked_data[1133], 4)
        chaikin_changeValue6 = round(unpacked_data[1134], 4)
        chaikin_changeValue7 = round(unpacked_data[1135], 4)
        chaikin_changeValue8 = round(unpacked_data[1136], 4)
        chaikin_changeValue9 = round(unpacked_data[1137], 4)
        chaikin_changeValue10 = round(unpacked_data[1138], 4)
        deMarker_changeValue1 = round(unpacked_data[1139], 4)
        deMarker_changeValue2 = round(unpacked_data[1140], 4)
        deMarker_changeValue3 = round(unpacked_data[1141], 4)
        deMarker_changeValue4 = round(unpacked_data[1142], 4)
        deMarker_changeValue5 = round(unpacked_data[1143], 4)
        deMarker_changeValue6 = round(unpacked_data[1144], 4)
        deMarker_changeValue7 = round(unpacked_data[1145], 4)
        deMarker_changeValue8 = round(unpacked_data[1146], 4)
        deMarker_changeValue9 = round(unpacked_data[1147], 4)
        deMarker_changeValue10 = round(unpacked_data[1148], 4)
        force_changeValue1 = round(unpacked_data[1149], 4)
        force_changeValue2 = round(unpacked_data[1150], 4)
        force_changeValue3 = round(unpacked_data[1151], 4)
        force_changeValue4 = round(unpacked_data[1152], 4)
        force_changeValue5 = round(unpacked_data[1153], 4)
        force_changeValue6 = round(unpacked_data[1154], 4)
        force_changeValue7 = round(unpacked_data[1155], 4)
        force_changeValue8 = round(unpacked_data[1156], 4)
        force_changeValue9 = round(unpacked_data[1157], 4)
        force_changeValue10 = round(unpacked_data[1158], 4)
        bwmfi_changeValue1 = round(unpacked_data[1159], 4)
        bwmfi_changeValue2 = round(unpacked_data[1160], 4)
        bwmfi_changeValue3 = round(unpacked_data[1161], 4)
        bwmfi_changeValue4 = round(unpacked_data[1162], 4)
        bwmfi_changeValue5 = round(unpacked_data[1163], 4)
        bwmfi_changeValue6 = round(unpacked_data[1164], 4)
        bwmfi_changeValue7 = round(unpacked_data[1165], 4)
        bwmfi_changeValue8 = round(unpacked_data[1166], 4)
        bwmfi_changeValue9 = round(unpacked_data[1167], 4)
        bwmfi_changeValue10 = round(unpacked_data[1168], 4)
        momentum_changeValue1 = round(unpacked_data[1169], 4)
        momentum_changeValue2 = round(unpacked_data[1170], 4)
        momentum_changeValue3 = round(unpacked_data[1171], 4)
        momentum_changeValue4 = round(unpacked_data[1172], 4)
        momentum_changeValue5 = round(unpacked_data[1173], 4)
        momentum_changeValue6 = round(unpacked_data[1174], 4)
        momentum_changeValue7 = round(unpacked_data[1175], 4)
        momentum_changeValue8 = round(unpacked_data[1176], 4)
        momentum_changeValue9 = round(unpacked_data[1177], 4)
        momentum_changeValue10 = round(unpacked_data[1178], 4)
        mfi_changeValue1 = round(unpacked_data[1179], 4)
        mfi_changeValue2 = round(unpacked_data[1180], 4)
        mfi_changeValue3 = round(unpacked_data[1181], 4)
        mfi_changeValue4 = round(unpacked_data[1182], 4)
        mfi_changeValue5 = round(unpacked_data[1183], 4)
        mfi_changeValue6 = round(unpacked_data[1184], 4)
        mfi_changeValue7 = round(unpacked_data[1185], 4)
        mfi_changeValue8 = round(unpacked_data[1186], 4)
        mfi_changeValue9 = round(unpacked_data[1187], 4)
        mfi_changeValue10 = round(unpacked_data[1188], 4)
        osMA_changeValue1 = round(unpacked_data[1189], 4)
        osMA_changeValue2 = round(unpacked_data[1190], 4)
        osMA_changeValue3 = round(unpacked_data[1191], 4)
        osMA_changeValue4 = round(unpacked_data[1192], 4)
        osMA_changeValue5 = round(unpacked_data[1193], 4)
        osMA_changeValue6 = round(unpacked_data[1194], 4)
        osMA_changeValue7 = round(unpacked_data[1195], 4)
        osMA_changeValue8 = round(unpacked_data[1196], 4)
        osMA_changeValue9 = round(unpacked_data[1197], 4)
        osMA_changeValue10 = round(unpacked_data[1198], 4)
        rvi_changeValue1 = round(unpacked_data[1199], 4)
        rvi_changeValue2 = round(unpacked_data[1200], 4)
        rvi_changeValue3 = round(unpacked_data[1201], 4)
        rvi_changeValue4 = round(unpacked_data[1202], 4)
        rvi_changeValue5 = round(unpacked_data[1203], 4)
        rvi_changeValue6 = round(unpacked_data[1204], 4)
        rvi_changeValue7 = round(unpacked_data[1205], 4)
        rvi_changeValue8 = round(unpacked_data[1206], 4)
        rvi_changeValue9 = round(unpacked_data[1207], 4)
        rvi_changeValue10 = round(unpacked_data[1208], 4)
        stdDev_changeValue1 = round(unpacked_data[1209], 4)
        stdDev_changeValue2 = round(unpacked_data[1210], 4)
        stdDev_changeValue3 = round(unpacked_data[1211], 4)
        stdDev_changeValue4 = round(unpacked_data[1212], 4)
        stdDev_changeValue5 = round(unpacked_data[1213], 4)
        stdDev_changeValue6 = round(unpacked_data[1214], 4)
        stdDev_changeValue7 = round(unpacked_data[1215], 4)
        stdDev_changeValue8 = round(unpacked_data[1216], 4)
        stdDev_changeValue9 = round(unpacked_data[1217], 4)
        stdDev_changeValue10 = round(unpacked_data[1218], 4)
        wpr_changeValue1 = round(unpacked_data[1219], 4)
        wpr_changeValue2 = round(unpacked_data[1220], 4)
        wpr_changeValue3 = round(unpacked_data[1221], 4)
        wpr_changeValue4 = round(unpacked_data[1222], 4)
        wpr_changeValue5 = round(unpacked_data[1223], 4)
        wpr_changeValue6 = round(unpacked_data[1224], 4)
        wpr_changeValue7 = round(unpacked_data[1225], 4)
        wpr_changeValue8 = round(unpacked_data[1226], 4)
        wpr_changeValue9 = round(unpacked_data[1227], 4)
        wpr_changeValue10 = round(unpacked_data[1228], 4)
        his_interval = round(unpacked_data[1229], 4)
        interval_10 = round(unpacked_data[1230], 4)
        interval_20 = round(unpacked_data[1231], 4)
        interval_30 = round(unpacked_data[1232], 4)

        data_list.append([volume,
                          atr5, atr10,
                          atr5_change1, atr5_change2, atr5_change3, atr5_change4, atr5_change5,
                          atr5_change6, atr5_change7, atr5_change8, atr5_change9, atr5_change10,
                          atr5_current_change1, atr5_current_change2, atr5_current_change3, atr5_current_change4,
                          atr5_current_change5,
                          atr5_current_change6, atr5_current_change7, atr5_current_change8, atr5_current_change9,
                          atr5_current_change10,
                          atr10_change1, atr10_change2, atr10_change3, atr10_change4, atr10_change5,
                          atr10_change6, atr10_change7, atr10_change8, atr10_change9, atr10_change10,
                          atr10_current_change1, atr10_current_change2, atr10_current_change3, atr10_current_change4,
                          atr10_current_change5,
                          atr10_current_change6, atr10_current_change7, atr10_current_change8, atr10_current_change9,
                          atr10_current_change10,
                          macd,
                          macd_change1, macd_change2, macd_change3, macd_change4, macd_change5,
                          macd_change6, macd_change7, macd_change8, macd_change9, macd_change10,
                          macd_current_change1, macd_current_change2, macd_current_change3, macd_current_change4,
                          macd_current_change5,
                          macd_current_change6, macd_current_change7, macd_current_change8, macd_current_change9,
                          macd_current_change10,
                          sma5, sma10,
                          sma5_change1, sma5_change2, sma5_change3, sma5_change4, sma5_change5,
                          sma5_change6, sma5_change7, sma5_change8, sma5_change9, sma5_change10,
                          sma5_current_change1, sma5_current_change2, sma5_current_change3, sma5_current_change4,
                          sma5_current_change5,
                          sma5_current_change6, sma5_current_change7, sma5_current_change8, sma5_current_change9,
                          sma5_current_change10,
                          sma10_change1, sma10_change2, sma10_change3, sma10_change4, sma10_change5,
                          sma10_change6, sma10_change7, sma10_change8, sma10_change9, sma10_change10,
                          sma10_current_change1, sma10_current_change2, sma10_current_change3, sma10_current_change4,
                          sma10_current_change5,
                          sma10_current_change6, sma10_current_change7, sma10_current_change8, sma10_current_change9,
                          sma10_current_change10,
                          ema5, ema10,
                          ema5_change1, ema5_change2, ema5_change3, ema5_change4, ema5_change5,
                          ema5_change6, ema5_change7, ema5_change8, ema5_change9, ema5_change10,
                          ema5_current_change1, ema5_current_change2, ema5_current_change3, ema5_current_change4,
                          ema5_current_change5,
                          ema5_current_change6, ema5_current_change7, ema5_current_change8, ema5_current_change9,
                          ema5_current_change10,
                          ema10_change1, ema10_change2, ema10_change3, ema10_change4, ema10_change5,
                          ema10_change6, ema10_change7, ema10_change8, ema10_change9, ema10_change10,
                          ema10_current_change1, ema10_current_change2, ema10_current_change3, ema10_current_change4,
                          ema10_current_change5,
                          ema10_current_change6, ema10_current_change7, ema10_current_change8, ema10_current_change9,
                          ema10_current_change10,
                          smma5, smma10,
                          smma5_change1, smma5_change2, smma5_change3, smma5_change4, smma5_change5,
                          smma5_change6, smma5_change7, smma5_change8, smma5_change9, smma5_change10,
                          smma5_current_change1, smma5_current_change2, smma5_current_change3, smma5_current_change4,
                          smma5_current_change5,
                          smma5_current_change6, smma5_current_change7, smma5_current_change8, smma5_current_change9,
                          smma5_current_change10,
                          smma10_change1, smma10_change2, smma10_change3, smma10_change4, smma10_change5,
                          smma10_change6, smma10_change7, smma10_change8, smma10_change9, smma10_change10,
                          smma10_current_change1, smma10_current_change2, smma10_current_change3,
                          smma10_current_change4,
                          smma10_current_change5,
                          smma10_current_change6, smma10_current_change7, smma10_current_change8,
                          smma10_current_change9,
                          smma10_current_change10,
                          lwma5, lwma10,
                          lwma5_change1, lwma5_change2, lwma5_change3, lwma5_change4, lwma5_change5,
                          lwma5_change6, lwma5_change7, lwma5_change8, lwma5_change9, lwma5_change10,
                          lwma5_current_change1, lwma5_current_change2, lwma5_current_change3, lwma5_current_change4,
                          lwma5_current_change5,
                          lwma5_current_change6, lwma5_current_change7, lwma5_current_change8, lwma5_current_change9,
                          lwma5_current_change10,
                          lwma10_change1, lwma10_change2, lwma10_change3, lwma10_change4, lwma10_change5,
                          lwma10_change6, lwma10_change7, lwma10_change8, lwma10_change9, lwma10_change10,
                          lwma10_current_change1, lwma10_current_change2, lwma10_current_change3,
                          lwma10_current_change4,
                          lwma10_current_change5,
                          lwma10_current_change6, lwma10_current_change7, lwma10_current_change8,
                          lwma10_current_change9,
                          lwma10_current_change10,
                          rsi5, rsi14,
                          rsi5_change1, rsi5_change2, rsi5_change3, rsi5_change4, rsi5_change5,
                          rsi5_change6, rsi5_change7, rsi5_change8, rsi5_change9, rsi5_change10,
                          rsi5_current_change1, rsi5_current_change2, rsi5_current_change3, rsi5_current_change4,
                          rsi5_current_change5,
                          rsi5_current_change6, rsi5_current_change7, rsi5_current_change8, rsi5_current_change9,
                          rsi5_current_change10,
                          rsi14_change1, rsi14_change2, rsi14_change3, rsi14_change4, rsi14_change5,
                          rsi14_change6, rsi14_change7, rsi14_change8, rsi14_change9, rsi14_change10,
                          rsi14_current_change1, rsi14_current_change2, rsi14_current_change3,
                          rsi14_current_change4,
                          rsi14_current_change5,
                          rsi14_current_change6, rsi14_current_change7, rsi14_current_change8,
                          rsi14_current_change9,
                          rsi14_current_change10,
                          sar,
                          sar_change1, sar_change2, sar_change3, sar_change4, sar_change5,
                          sar_change6, sar_change7, sar_change8, sar_change9, sar_change10,
                          sar_current_change1, sar_current_change2, sar_current_change3, sar_current_change4,
                          sar_current_change5,
                          sar_current_change6, sar_current_change7, sar_current_change8, sar_current_change9,
                          sar_current_change10,
                          adx, adx_DI_plus, adx_DI_minus,
                          adx_change1, adx_change2, adx_change3, adx_change4, adx_change5,
                          adx_change6, adx_change7, adx_change8, adx_change9, adx_change10,
                          adx_current_change1, adx_current_change2, adx_current_change3, adx_current_change4,
                          adx_current_change5,
                          adx_current_change6, adx_current_change7, adx_current_change8, adx_current_change9,
                          adx_current_change10,
                          cci,
                          cci_change1, cci_change2, cci_change3, cci_change4, cci_change5,
                          cci_change6, cci_change7, cci_change8, cci_change9, cci_change10,
                          cci_current_change1, cci_current_change2, cci_current_change3, cci_current_change4,
                          cci_current_change5,
                          cci_current_change6, cci_current_change7, cci_current_change8, cci_current_change9,
                          cci_current_change10,
                          slowk, slowd,
                          slowk_change1, slowk_change2, slowk_change3, slowk_change4, slowk_change5,
                          slowk_change6, slowk_change7, slowk_change8, slowk_change9, slowk_change10,
                          slowk_current_change1, slowk_current_change2, slowk_current_change3, slowk_current_change4,
                          slowk_current_change5,
                          slowk_current_change6, slowk_current_change7, slowk_current_change8, slowk_current_change9,
                          slowk_current_change10,
                          boll_upper_band, boll_middle_band, boll_lower_band,
                          boll_change1, boll_change2, boll_change3, boll_change4, boll_change5,
                          boll_change6, boll_change7, boll_change8, boll_change9, boll_change10,
                          boll_current_change1, boll_current_change2, boll_current_change3, boll_current_change4,
                          boll_current_change5,
                          boll_current_change6, boll_current_change7, boll_current_change8, boll_current_change9,
                          boll_current_change10,
                          ac_value, ac_color,
                          ac_change1, ac_change2, ac_change3, ac_change4, ac_change5,
                          ac_change6, ac_change7, ac_change8, ac_change9, ac_change10,
                          ac_current_change1, ac_current_change2, ac_current_change3, ac_current_change4,
                          ac_current_change5,
                          ac_current_change6, ac_current_change7, ac_current_change8, ac_current_change9,
                          ac_current_change10,
                          ad,
                          ad_change1, ad_change2, ad_change3, ad_change4, ad_change5,
                          ad_change6, ad_change7, ad_change8, ad_change9, ad_change10,
                          ad_current_change1, ad_current_change2, ad_current_change3, ad_current_change4,
                          ad_current_change5,
                          ad_current_change6, ad_current_change7, ad_current_change8, ad_current_change9,
                          ad_current_change10,
                          adxWilder, adxWilder_DI_plus, adxWilder_DI_minus,
                          adxWilder_change1, adxWilder_change2, adxWilder_change3, adxWilder_change4, adxWilder_change5,
                          adxWilder_change6, adxWilder_change7, adxWilder_change8, adxWilder_change9,
                          adxWilder_change10,
                          adxWilder_current_change1, adxWilder_current_change2, adxWilder_current_change3,
                          adxWilder_current_change4,
                          adxWilder_current_change5,
                          adxWilder_current_change6, adxWilder_current_change7, adxWilder_current_change8,
                          adxWilder_current_change9,
                          adxWilder_current_change10,
                          jaws, teeth, lips,
                          lips_change1, lips_change2, lips_change3, lips_change4, lips_change5,
                          lips_change6, lips_change7, lips_change8, lips_change9,
                          lips_change10,
                          lips_current_change1, lips_current_change2, lips_current_change3, lips_current_change4,
                          lips_current_change5,
                          lips_current_change6, lips_current_change7, lips_current_change8, lips_current_change9,
                          lips_current_change10,
                          ama,
                          ama_change1, ama_change2, ama_change3, ama_change4, ama_change5,
                          ama_change6, ama_change7, ama_change8, ama_change9,
                          ama_change10,
                          ama_current_change1, ama_current_change2, ama_current_change3, ama_current_change4,
                          ama_current_change5,
                          ama_current_change6, ama_current_change7, ama_current_change8, ama_current_change9,
                          ama_current_change10,
                          ao_value, ao_color,
                          ao_change1, ao_change2, ao_change3, ao_change4, ao_change5,
                          ao_change6, ao_change7, ao_change8, ao_change9,
                          ao_change10,
                          ao_current_change1, ao_current_change2, ao_current_change3, ao_current_change4,
                          ao_current_change5,
                          ao_current_change6, ao_current_change7, ao_current_change8, ao_current_change9,
                          ao_current_change10,
                          bearsPower,
                          bears_change1, bears_change2, bears_change3, bears_change4, bears_change5,
                          bears_change6, bears_change7, bears_change8, bears_change9,
                          bears_change10,
                          bears_current_change1, bears_current_change2, bears_current_change3, bears_current_change4,
                          bears_current_change5,
                          bears_current_change6, bears_current_change7, bears_current_change8, bears_current_change9,
                          bears_current_change10,
                          bullsPower,
                          bulls_change1, bulls_change2, bulls_change3, bulls_change4, bulls_change5,
                          bulls_change6, bulls_change7, bulls_change8, bulls_change9,
                          bulls_change10,
                          bulls_current_change1, bulls_current_change2, bulls_current_change3, bulls_current_change4,
                          bulls_current_change5,
                          bulls_current_change6, bulls_current_change7, bulls_current_change8, bulls_current_change9,
                          bulls_current_change10,
                          chaikin,
                          chaikin_change1, chaikin_change2, chaikin_change3, chaikin_change4, chaikin_change5,
                          chaikin_change6, chaikin_change7, chaikin_change8, chaikin_change9,
                          chaikin_change10,
                          chaikin_current_change1, chaikin_current_change2, chaikin_current_change3,
                          chaikin_current_change4,
                          chaikin_current_change5,
                          chaikin_current_change6, chaikin_current_change7, chaikin_current_change8,
                          chaikin_current_change9,
                          chaikin_current_change10,
                          dema,
                          dema_change1, dema_change2, dema_change3, dema_change4, dema_change5,
                          dema_change6, dema_change7, dema_change8, dema_change9,
                          dema_change10,
                          dema_current_change1, dema_current_change2, dema_current_change3,
                          dema_current_change4,
                          dema_current_change5,
                          dema_current_change6, dema_current_change7, dema_current_change8,
                          dema_current_change9,
                          dema_current_change10,
                          deMarker,
                          deMarker_change1, deMarker_change2, deMarker_change3, deMarker_change4, deMarker_change5,
                          deMarker_change6, deMarker_change7, deMarker_change8, deMarker_change9,
                          deMarker_change10,
                          deMarker_current_change1, deMarker_current_change2, deMarker_current_change3,
                          deMarker_current_change4,
                          deMarker_current_change5,
                          deMarker_current_change6, deMarker_current_change7, deMarker_current_change8,
                          deMarker_current_change9,
                          deMarker_current_change10,
                          envelopes_upper_value, envelopes_lower_value,
                          force,
                          force_change1, force_change2, force_change3, force_change4, force_change5,
                          force_change6, force_change7, force_change8, force_change9,
                          force_change10,
                          force_current_change1, force_current_change2, force_current_change3,
                          force_current_change4,
                          force_current_change5,
                          force_current_change6, force_current_change7, force_current_change8,
                          force_current_change9,
                          force_current_change10,
                          fractals_up_arrow, fractals_down_arrow,
                          frAMA,
                          frAMA_change1, frAMA_change2, frAMA_change3, frAMA_change4, frAMA_change5,
                          frAMA_change6, frAMA_change7, frAMA_change8, frAMA_change9,
                          frAMA_change10,
                          frAMA_current_change1, frAMA_current_change2, frAMA_current_change3,
                          frAMA_current_change4,
                          frAMA_current_change5,
                          frAMA_current_change6, frAMA_current_change7, frAMA_current_change8,
                          frAMA_current_change9,
                          frAMA_current_change10,
                          gator_ups, gator_up_color, gator_downs, gator_downs_color,
                          tenkan_sen, kijun_sen, senkou_span_A, senkou_span_B, chinkou_span,
                          bwmfi_value, bwmfi_color,
                          bwmfi_change1, bwmfi_change2, bwmfi_change3, bwmfi_change4, bwmfi_change5,
                          bwmfi_change6, bwmfi_change7, bwmfi_change8, bwmfi_change9,
                          bwmfi_change10,
                          bwmfi_current_change1, bwmfi_current_change2, bwmfi_current_change3,
                          bwmfi_current_change4,
                          bwmfi_current_change5,
                          bwmfi_current_change6, bwmfi_current_change7, bwmfi_current_change8,
                          bwmfi_current_change9,
                          bwmfi_current_change10,
                          momentum,
                          momentum_change1, momentum_change2, momentum_change3, momentum_change4, momentum_change5,
                          momentum_change6, momentum_change7, momentum_change8, momentum_change9,
                          momentum_change10,
                          momentum_current_change1, momentum_current_change2, momentum_current_change3,
                          momentum_current_change4,
                          momentum_current_change5,
                          momentum_current_change6, momentum_current_change7, momentum_current_change8,
                          momentum_current_change9,
                          momentum_current_change10,
                          mfi,
                          mfi_change1, mfi_change2, mfi_change3, mfi_change4, mfi_change5,
                          mfi_change6, mfi_change7, mfi_change8, mfi_change9,
                          mfi_change10,
                          mfi_current_change1, mfi_current_change2, mfi_current_change3,
                          mfi_current_change4,
                          mfi_current_change5,
                          mfi_current_change6, mfi_current_change7, mfi_current_change8,
                          mfi_current_change9,
                          mfi_current_change10,
                          osMA,
                          osMA_change1, osMA_change2, osMA_change3, osMA_change4, osMA_change5,
                          osMA_change6, osMA_change7, osMA_change8, osMA_change9,
                          osMA_change10,
                          osMA_current_change1, osMA_current_change2, osMA_current_change3,
                          osMA_current_change4,
                          osMA_current_change5,
                          osMA_current_change6, osMA_current_change7, osMA_current_change8,
                          osMA_current_change9,
                          osMA_current_change10,
                          obv,
                          obv_change1, obv_change2, obv_change3, obv_change4, obv_change5,
                          obv_change6, obv_change7, obv_change8, obv_change9,
                          obv_change10,
                          obv_current_change1, obv_current_change2, obv_current_change3,
                          obv_current_change4,
                          obv_current_change5,
                          obv_current_change6, obv_current_change7, obv_current_change8,
                          obv_current_change9,
                          obv_current_change10,
                          rvi, rvi_signal,
                          rvi_change1, rvi_change2, rvi_change3, rvi_change4, rvi_change5,
                          rvi_change6, rvi_change7, rvi_change8, rvi_change9,
                          rvi_change10,
                          rvi_current_change1, rvi_current_change2, rvi_current_change3,
                          rvi_current_change4,
                          rvi_current_change5,
                          rvi_current_change6, rvi_current_change7, rvi_current_change8,
                          rvi_current_change9,
                          rvi_current_change10,
                          stdDev,
                          stdDev_change1, stdDev_change2, stdDev_change3, stdDev_change4, stdDev_change5,
                          stdDev_change6, stdDev_change7, stdDev_change8, stdDev_change9,
                          stdDev_change10,
                          stdDev_current_change1, stdDev_current_change2, stdDev_current_change3,
                          stdDev_current_change4,
                          stdDev_current_change5,
                          stdDev_current_change6, stdDev_current_change7, stdDev_current_change8,
                          stdDev_current_change9,
                          stdDev_current_change10,
                          tema,
                          tema_change1, tema_change2, tema_change3, tema_change4, tema_change5,
                          tema_change6, tema_change7, tema_change8, tema_change9,
                          tema_change10,
                          tema_current_change1, tema_current_change2, tema_current_change3,
                          tema_current_change4,
                          tema_current_change5,
                          tema_current_change6, tema_current_change7, tema_current_change8,
                          tema_current_change9,
                          tema_current_change10,
                          triX,
                          triX_change1, triX_change2, triX_change3, triX_change4, triX_change5,
                          triX_change6, triX_change7, triX_change8, triX_change9,
                          triX_change10,
                          triX_current_change1, triX_current_change2, triX_current_change3,
                          triX_current_change4,
                          triX_current_change5,
                          triX_current_change6, triX_current_change7, triX_current_change8,
                          triX_current_change9,
                          triX_current_change10,
                          wpr,
                          wpr_change1, wpr_change2, wpr_change3, wpr_change4, wpr_change5,
                          wpr_change6, wpr_change7, wpr_change8, wpr_change9,
                          wpr_change10,
                          wpr_current_change1, wpr_current_change2, wpr_current_change3,
                          wpr_current_change4,
                          wpr_current_change5,
                          wpr_current_change6, wpr_current_change7, wpr_current_change8,
                          wpr_current_change9,
                          wpr_current_change10,
                          vidya,
                          vidya_change1, vidya_change2, vidya_change3, vidya_change4, vidya_change5,
                          vidya_change6, vidya_change7, vidya_change8, vidya_change9,
                          vidya_change10,
                          vidya_current_change1, vidya_current_change2, vidya_current_change3,
                          vidya_current_change4,
                          vidya_current_change5,
                          vidya_current_change6, vidya_current_change7, vidya_current_change8,
                          vidya_current_change9,
                          vidya_current_change10,
                          atr_5_10_type,
                          macd_type,
                          sma_5_10_type,
                          ema_5_10_type,
                          smma_5_10_type,
                          lwma_5_10_type,
                          rsi_5_14_type,
                          sar_type,
                          adx_type,
                          cci_type,
                          stoch_type,
                          boll_type,
                          ac_type,
                          ad_type,
                          adxWilder_type,
                          alligator_type,
                          ama_type,
                          ao_type,
                          bearsPower_type,
                          bullsPower_type,
                          chaikin_type,
                          dema_type,
                          deMarker_type,
                          envelopes_type,
                          force_type,
                          fractals_type,
                          frAMA_type,
                          gator_type,
                          ichimoku_type,
                          bwmfi_type,
                          momentum_type,
                          mfi_type,
                          osMA_type,
                          obv_type,
                          rvi_type,
                          stdDev_type,
                          tema_type,
                          triX_type,
                          wpr_type,
                          vidya_type,
                          atr5_changeValue1, atr5_changeValue2, atr5_changeValue3, atr5_changeValue4,
                          atr5_changeValue5, atr5_changeValue6, atr5_changeValue7, atr5_changeValue8,
                          atr5_changeValue9, atr5_changeValue10,
                          atr10_changeValue1, atr10_changeValue2, atr10_changeValue3, atr10_changeValue4,
                          atr10_changeValue5, atr10_changeValue6, atr10_changeValue7, atr10_changeValue8,
                          atr10_changeValue9, atr10_changeValue10,
                          macd_changeValue1, macd_changeValue2, macd_changeValue3, macd_changeValue4,
                          macd_changeValue5, macd_changeValue6, macd_changeValue7, macd_changeValue8,
                          macd_changeValue9, macd_changeValue10,
                          sma5_changeValue1, sma5_changeValue2, sma5_changeValue3, sma5_changeValue4,
                          sma5_changeValue5, sma5_changeValue6, sma5_changeValue7, sma5_changeValue8,
                          sma5_changeValue9, sma5_changeValue10,
                          sma10_changeValue1, sma10_changeValue2, sma10_changeValue3, sma10_changeValue4,
                          sma10_changeValue5, sma10_changeValue6, sma10_changeValue7, sma10_changeValue8,
                          sma10_changeValue9, sma10_changeValue10,
                          rsi5_changeValue1, rsi5_changeValue2, rsi5_changeValue3, rsi5_changeValue4,
                          rsi5_changeValue5, rsi5_changeValue6, rsi5_changeValue7, rsi5_changeValue8,
                          rsi5_changeValue9, rsi5_changeValue10,
                          rsi14_changeValue1, rsi14_changeValue2, rsi14_changeValue3, rsi14_changeValue4,
                          rsi14_changeValue5, rsi14_changeValue6, rsi14_changeValue7, rsi14_changeValue8,
                          rsi14_changeValue9, rsi14_changeValue10,
                          sar_changeValue1, sar_changeValue2, sar_changeValue3, sar_changeValue4,
                          sar_changeValue5, sar_changeValue6, sar_changeValue7, sar_changeValue8,
                          sar_changeValue9, sar_changeValue10,
                          adx_changeValue1, adx_changeValue2, adx_changeValue3, adx_changeValue4,
                          adx_changeValue5, adx_changeValue6, adx_changeValue7, adx_changeValue8,
                          adx_changeValue9, adx_changeValue10,
                          cci_changeValue1, cci_changeValue2, cci_changeValue3, cci_changeValue4,
                          cci_changeValue5, cci_changeValue6, cci_changeValue7, cci_changeValue8,
                          cci_changeValue9, cci_changeValue10,
                          slowk_changeValue1, slowk_changeValue2, slowk_changeValue3, slowk_changeValue4,
                          slowk_changeValue5, slowk_changeValue6, slowk_changeValue7, slowk_changeValue8,
                          slowk_changeValue9, slowk_changeValue10,
                          ac_changeValue1, ac_changeValue2, ac_changeValue3, ac_changeValue4,
                          ac_changeValue5, ac_changeValue6, ac_changeValue7, ac_changeValue8,
                          ac_changeValue9, ac_changeValue10,
                          adxWilder_changeValue1, adxWilder_changeValue2, adxWilder_changeValue3,
                          adxWilder_changeValue4,
                          adxWilder_changeValue5, adxWilder_changeValue6, adxWilder_changeValue7,
                          adxWilder_changeValue8,
                          adxWilder_changeValue9, adxWilder_changeValue10,
                          lips_changeValue1, lips_changeValue2, lips_changeValue3, lips_changeValue4,
                          lips_changeValue5, lips_changeValue6, lips_changeValue7, lips_changeValue8,
                          lips_changeValue9, lips_changeValue10,
                          ama_changeValue1, ama_changeValue2, ama_changeValue3, ama_changeValue4,
                          ama_changeValue5, ama_changeValue6, ama_changeValue7, ama_changeValue8,
                          ama_changeValue9, ama_changeValue10,
                          ao_changeValue1, ao_changeValue2, ao_changeValue3, ao_changeValue4,
                          ao_changeValue5, ao_changeValue6, ao_changeValue7, ao_changeValue8,
                          ao_changeValue9, ao_changeValue10,
                          bears_changeValue1, bears_changeValue2, bears_changeValue3, bears_changeValue4,
                          bears_changeValue5, bears_changeValue6, bears_changeValue7, bears_changeValue8,
                          bears_changeValue9, bears_changeValue10,
                          bulls_changeValue1, bulls_changeValue2, bulls_changeValue3, bulls_changeValue4,
                          bulls_changeValue5, bulls_changeValue6, bulls_changeValue7, bulls_changeValue8,
                          bulls_changeValue9, bulls_changeValue10,
                          chaikin_changeValue1, chaikin_changeValue2, chaikin_changeValue3, chaikin_changeValue4,
                          chaikin_changeValue5, chaikin_changeValue6, chaikin_changeValue7, chaikin_changeValue8,
                          chaikin_changeValue9, chaikin_changeValue10,
                          deMarker_changeValue1, deMarker_changeValue2, deMarker_changeValue3, deMarker_changeValue4,
                          deMarker_changeValue5, deMarker_changeValue6, deMarker_changeValue7, deMarker_changeValue8,
                          deMarker_changeValue9, deMarker_changeValue10,
                          force_changeValue1, force_changeValue2, force_changeValue3, force_changeValue4,
                          force_changeValue5, force_changeValue6, force_changeValue7, force_changeValue8,
                          force_changeValue9, force_changeValue10,
                          bwmfi_changeValue1, bwmfi_changeValue2, bwmfi_changeValue3, bwmfi_changeValue4,
                          bwmfi_changeValue5, bwmfi_changeValue6, bwmfi_changeValue7, bwmfi_changeValue8,
                          bwmfi_changeValue9, bwmfi_changeValue10,
                          momentum_changeValue1, momentum_changeValue2, momentum_changeValue3, momentum_changeValue4,
                          momentum_changeValue5, momentum_changeValue6, momentum_changeValue7, momentum_changeValue8,
                          momentum_changeValue9, momentum_changeValue10,
                          mfi_changeValue1, mfi_changeValue2, mfi_changeValue3, mfi_changeValue4,
                          mfi_changeValue5, mfi_changeValue6, mfi_changeValue7, mfi_changeValue8,
                          mfi_changeValue9, mfi_changeValue10,
                          osMA_changeValue1, osMA_changeValue2, osMA_changeValue3, osMA_changeValue4,
                          osMA_changeValue5, osMA_changeValue6, osMA_changeValue7, osMA_changeValue8,
                          osMA_changeValue9, osMA_changeValue10,
                          rvi_changeValue1, rvi_changeValue2, rvi_changeValue3, rvi_changeValue4,
                          rvi_changeValue5, rvi_changeValue6, rvi_changeValue7, rvi_changeValue8,
                          rvi_changeValue9, rvi_changeValue10,
                          stdDev_changeValue1, stdDev_changeValue2, stdDev_changeValue3, stdDev_changeValue4,
                          stdDev_changeValue5, stdDev_changeValue6, stdDev_changeValue7, stdDev_changeValue8,
                          stdDev_changeValue9, stdDev_changeValue10,
                          wpr_changeValue1, wpr_changeValue2, wpr_changeValue3, wpr_changeValue4,
                          wpr_changeValue5, wpr_changeValue6, wpr_changeValue7, wpr_changeValue8,
                          wpr_changeValue9, wpr_changeValue10,
                          his_interval, interval_10, interval_20, interval_30
                          ])

        clm = ['volume',
               'atr5', 'atr10',
               'atr5_change1', 'atr5_change2', 'atr5_change3', 'atr5_change4', 'atr5_change5',
               'atr5_change6', 'atr5_change7', 'atr5_change8', 'atr5_change9', 'atr5_change10',
               'atr5_current_change1', 'atr5_current_change2', 'atr5_current_change3', 'atr5_current_change4',
               'atr5_current_change5',
               'atr5_current_change6', 'atr5_current_change7', 'atr5_current_change8', 'atr5_current_change9',
               'atr5_current_change10',
               'atr10_change1', 'atr10_change2', 'atr10_change3', 'atr10_change4', 'atr10_change5',
               'atr10_change6', 'atr10_change7', 'atr10_change8', 'atr10_change9', 'atr10_change10',
               'atr10_current_change1', 'atr10_current_change2', 'atr10_current_change3', 'atr10_current_change4',
               'atr10_current_change5',
               'atr10_current_change6', 'atr10_current_change7', 'atr10_current_change8', 'atr10_current_change9',
               'atr10_current_change10',
               'macd',
               'macd_change1', 'macd_change2', 'macd_change3', 'macd_change4', 'macd_change5',
               'macd_change6', 'macd_change7', 'macd_change8', 'macd_change9', 'macd_change10',
               'macd_current_change1', 'macd_current_change2', 'macd_current_change3', 'macd_current_change4',
               'macd_current_change5',
               'macd_current_change6', 'macd_current_change7', 'macd_current_change8', 'macd_current_change9',
               'macd_current_change10',
               'sma5', 'sma10',
               'sma5_change1', 'sma5_change2', 'sma5_change3', 'sma5_change4', 'sma5_change5',
               'sma5_change6', 'sma5_change7', 'sma5_change8', 'sma5_change9', 'sma5_change10',
               'sma5_current_change1', 'sma5_current_change2', 'sma5_current_change3', 'sma5_current_change4',
               'sma5_current_change5',
               'sma5_current_change6', 'sma5_current_change7', 'sma5_current_change8', 'sma5_current_change9',
               'sma5_current_change10',
               'sma10_change1', 'sma10_change2', 'sma10_change3', 'sma10_change4', 'sma10_change5',
               'sma10_change6', 'sma10_change7', 'sma10_change8', 'sma10_change9', 'sma10_change10',
               'sma10_current_change1', 'sma10_current_change2', 'sma10_current_change3', 'sma10_current_change4',
               'sma10_current_change5',
               'sma10_current_change6', 'sma10_current_change7', 'sma10_current_change8', 'sma10_current_change9',
               'sma10_current_change10',
               'ema5', 'ema10',
               'ema5_change1', 'ema5_change2', 'ema5_change3', 'ema5_change4', 'ema5_change5',
               'ema5_change6', 'ema5_change7', 'ema5_change8', 'ema5_change9', 'ema5_change10',
               'ema5_current_change1', 'ema5_current_change2', 'ema5_current_change3', 'ema5_current_change4',
               'ema5_current_change5',
               'ema5_current_change6', 'ema5_current_change7', 'ema5_current_change8', 'ema5_current_change9',
               'ema5_current_change10',
               'ema10_change1', 'ema10_change2', 'ema10_change3', 'ema10_change4', 'ema10_change5',
               'ema10_change6', 'ema10_change7', 'ema10_change8', 'ema10_change9', 'ema10_change10',
               'ema10_current_change1', 'ema10_current_change2', 'ema10_current_change3', 'ema10_current_change4',
               'ema10_current_change5',
               'ema10_current_change6', 'ema10_current_change7', 'ema10_current_change8', 'ema10_current_change9',
               'ema10_current_change10',
               'smma5', 'smma10',
               'smma5_change1', 'smma5_change2', 'smma5_change3', 'smma5_change4', 'smma5_change5',
               'smma5_change6', 'smma5_change7', 'smma5_change8', 'smma5_change9', 'smma5_change10',
               'smma5_current_change1', 'smma5_current_change2', 'smma5_current_change3', 'smma5_current_change4',
               'smma5_current_change5',
               'smma5_current_change6', 'smma5_current_change7', 'smma5_current_change8', 'smma5_current_change9',
               'smma5_current_change10',
               'smma10_change1', 'smma10_change2', 'smma10_change3', 'smma10_change4', 'smma10_change5',
               'smma10_change6', 'smma10_change7', 'smma10_change8', 'smma10_change9', 'smma10_change10',
               'smma10_current_change1', 'smma10_current_change2', 'smma10_current_change3', 'smma10_current_change4',
               'smma10_current_change5',
               'smma10_current_change6', 'smma10_current_change7', 'smma10_current_change8', 'smma10_current_change8',
               'smma10_current_change10',
               'lwma5', 'lwma10',
               'lwma5_change1', 'lwma5_change2', 'lwma5_change3', 'lwma5_change4', 'lwma5_change5',
               'lwma5_change6', 'lwma5_change7', 'lwma5_change8', 'lwma5_change9', 'lwma5_change10',
               'lwma5_current_change1', 'lwma5_current_change2', 'lwma5_current_change3', 'lwma5_current_change4',
               'lwma5_current_change5',
               'lwma5_current_change6', 'lwma5_current_change7', 'lwma5_current_change8', 'lwma5_current_change9',
               'lwma5_current_change10',
               'lwma10_change1', 'lwma10_change2', 'lwma10_change3', 'lwma10_change4', 'lwma10_change5',
               'lwma10_change6', 'lwma10_change7', 'lwma10_change8', 'lwma10_change9', 'lwma10_change10',
               'lwma10_current_change1', 'lwma10_current_change2', 'lwma10_current_change3',
               'lwma10_current_change4',
               'lwma10_current_change5',
               'lwma10_current_change6', 'lwma10_current_change7', 'lwma10_current_change8',
               'lwma10_current_change9',
               'lwma10_current_change10',
               'rsi5', 'rsi14',
               'rsi5_change1', 'rsi5_change2', 'rsi5_change3', 'rsi5_change4', 'rsi5_change5',
               'rsi5_change6', 'rsi5_change7', 'rsi5_change8', 'rsi5_change9', 'rsi5_change10',
               'rsi5_current_change1', 'rsi5_current_change2', 'rsi5_current_change3', 'rsi5_current_change4',
               'rsi5_current_change5',
               'rsi5_current_change6', 'rsi5_current_change7', 'rsi5_current_change8', 'rsi5_current_change9',
               'rsi5_current_change10',
               'rsi14_change1', 'rsi14_change2', 'rsi14_change3', 'rsi14_change4', 'rsi14_change5',
               'rsi14_change6', 'rsi14_change7', 'rsi14_change8', 'rsi14_change9', 'rsi14_change10',
               'rsi14_current_change1', 'rsi14_current_change2', 'rsi14_current_change3',
               'rsi14_current_change4',
               'rsi14_current_change5',
               'rsi14_current_change6', 'rsi14_current_change7', 'rsi14_current_change8',
               'rsi14_current_change9',
               'rsi14_current_change10',
               'sar',
               'sar_change1', 'sar_change2', 'sar_change3', 'sar_change4', 'sar_change5',
               'sar_change6', 'sar_change7', 'sar_change8', 'sar_change9', 'sar_change10',
               'sar_current_change1', 'sar_current_change2', 'sar_current_change3', 'sar_current_change4',
               'sar_current_change5',
               'sar_current_change6', 'sar_current_change7', 'sar_current_change8', 'sar_current_change9',
               'sar_current_change10',
               'adx', 'adx_DI_plus', 'adx_DI_minus',
               'adx_change1', 'adx_change2', 'adx_change3', 'adx_change4', 'adx_change5',
               'adx_change6', 'adx_change7', 'adx_change8', 'adx_change9', 'adx_change10',
               'adx_current_change1', 'adx_current_change2', 'adx_current_change3', 'adx_current_change4',
               'adx_current_change5',
               'adx_current_change6', 'adx_current_change7', 'adx_current_change8', 'adx_current_change9',
               'adx_current_change10',
               'cci',
               'cci_change1', 'cci_change2', 'cci_change3', 'cci_change4', 'cci_change5',
               'cci_change6', 'cci_change7', 'cci_change8', 'cci_change9', 'cci_change10',
               'cci_current_change1', 'cci_current_change2', 'cci_current_change3', 'cci_current_change4',
               'cci_current_change5',
               'cci_current_change6', 'cci_current_change7', 'cci_current_change8', 'cci_current_change9',
               'cci_current_change10',
               'slowk', 'slowd',
               'slowk_change1', 'slowk_change2', 'slowk_change3', 'slowk_change4', 'slowk_change5',
               'slowk_change6', 'slowk_change7', 'slowk_change8', 'slowk_change9', 'slowk_change10',
               'slowk_current_change1', 'slowk_current_change2', 'slowk_current_change3', 'slowk_current_change4',
               'slowk_current_change5',
               'slowk_current_change6', 'slowk_current_change7', 'slowk_current_change8', 'slowk_current_change9',
               'slowk_current_change10',
               'boll_upper_band', 'boll_middle_band', 'boll_lower_band',
               'boll_change1', 'boll_change2', 'boll_change3', 'boll_change4', 'boll_change5',
               'boll_change6', 'boll_change7', 'boll_change8', 'boll_change9', 'boll_change10',
               'boll_current_change1', 'boll_current_change2', 'boll_current_change3', 'boll_current_change4',
               'boll_current_change5',
               'boll_current_change6', 'boll_current_change7', 'boll_current_change8', 'boll_current_change9',
               'boll_current_change10',
               'ac_value', 'ac_color',
               'ac_change1', 'ac_change2', 'ac_change3', 'ac_change4', 'ac_change5',
               'ac_change6', 'ac_change7', 'ac_change8', 'ac_change9', 'ac_change10',
               'ac_current_change1', 'ac_current_change2', 'ac_current_change3', 'ac_current_change4',
               'ac_current_change5',
               'ac_current_change6', 'ac_current_change7', 'ac_current_change8', 'ac_current_change9',
               'ac_current_change10',
               'ad',
               'ad_change1', 'ad_change2', 'ad_change3', 'ad_change4', 'ad_change5',
               'ad_change6', 'ad_change7', 'ad_change8', 'ad_change9', 'ad_change10',
               'ad_current_change1', 'ad_current_change2', 'ad_current_change3', 'ad_current_change4',
               'ad_current_change5',
               'ad_current_change6', 'ad_current_change7', 'ad_current_change8', 'ad_current_change9',
               'ad_current_change10',
               'adxWilder', 'adxWilder_DI_plus', 'adxWilder_DI_minus',
               'adxWilder_change1', 'adxWilder_change2', 'adxWilder_change3', 'adxWilder_change4', 'adxWilder_change5',
               'adxWilder_change6', 'adxWilder_change7', 'adxWilder_change8', 'adxWilder_change9', 'adxWilder_change10',
               'adxWilder_current_change1', 'adxWilder_current_change2', 'adxWilder_current_change3',
               'adxWilder_current_change4',
               'adxWilder_current_change5',
               'adxWilder_current_change6', 'adxWilder_current_change7', 'adxWilder_current_change8',
               'adxWilder_current_change9',
               'adxWilder_current_change10',
               'jaws', 'teeth', 'lips',
               'lips_change1', 'lips_change2', 'lips_change3', 'lips_change4', 'lips_change5',
               'lips_change6', 'lips_change7', 'lips_change8', 'lips_change9',
               'lips_change10',
               'lips_current_change1', 'lips_current_change2', 'lips_current_change3', 'lips_current_change4',
               'lips_current_change5',
               'lips_current_change6', 'lips_current_change7', 'lips_current_change8', 'lips_current_change9',
               'lips_current_change10',
               'ama',
               'ama_change1', 'ama_change2', 'ama_change3', 'ama_change4', 'ama_change5',
               'ama_change6', 'ama_change7', 'ama_change8', 'ama_change9',
               'ama_change10',
               'ama_current_change1', 'ama_current_change2', 'ama_current_change3', 'ama_current_change4',
               'ama_current_change5',
               'ama_current_change6', 'ama_current_change7', 'ama_current_change8', 'ama_current_change9',
               'ama_current_change10',
               'ao_value', 'ao_color',
               'ao_change1', 'ao_change2', 'ao_change3', 'ao_change4', 'ao_change5',
               'ao_change6', 'ao_change7', 'ao_change8', 'ao_change9',
               'ao_change10',
               'ao_current_change1', 'ao_current_change2', 'ao_current_change3', 'ao_current_change4',
               'ao_current_change5',
               'ao_current_change6', 'ao_current_change7', 'ao_current_change8', 'ao_current_change9',
               'ao_current_change10',
               'bearsPower',
               'bears_change1', 'bears_change2', 'bears_change3', 'bears_change4', 'bears_change5',
               'bears_change6', 'bears_change7', 'bears_change8', 'bears_change9',
               'bears_change10',
               'bears_current_change1', 'bears_current_change2', 'bears_current_change3', 'bears_current_change4',
               'bears_current_change5',
               'bears_current_change6', 'bears_current_change7', 'bears_current_change8', 'bears_current_change9',
               'bears_current_change10',
               'bullsPower',
               'bulls_change1', 'bulls_change2', 'bulls_change3', 'bulls_change4', 'bulls_change5',
               'bulls_change6', 'bulls_change7', 'bulls_change8', 'bulls_change9',
               'bulls_change10',
               'bulls_current_change1', 'bulls_current_change2', 'bulls_current_change3', 'bulls_current_change4',
               'bulls_current_change5',
               'bulls_current_change6', 'bulls_current_change7', 'bulls_current_change8', 'bulls_current_change9',
               'bulls_current_change10',
               'chaikin',
               'chaikin_change1', 'chaikin_change2', 'chaikin_change3', 'chaikin_change4', 'chaikin_change5',
               'chaikin_change6', 'chaikin_change7', 'chaikin_change8', 'chaikin_change9',
               'chaikin_change10',
               'chaikin_current_change1', 'chaikin_current_change2', 'chaikin_current_change3',
               'chaikin_current_change4',
               'chaikin_current_change5',
               'chaikin_current_change6', 'chaikin_current_change7', 'chaikin_current_change8',
               'chaikin_current_change9',
               'chaikin_current_change10',
               'dema',
               'dema_change1', 'dema_change2', 'dema_change3', 'dema_change4', 'dema_change5',
               'dema_change6', 'dema_change7', 'dema_change8', 'dema_change9',
               'dema_change10',
               'dema_current_change1', 'dema_current_change2', 'dema_current_change3',
               'dema_current_change4',
               'dema_current_change5',
               'dema_current_change6', 'dema_current_change7', 'dema_current_change8',
               'dema_current_change9',
               'dema_current_change10',
               'deMarker',
               'deMarker_change1', 'deMarker_change2', 'deMarker_change3', 'deMarker_change4', 'deMarker_change5',
               'deMarker_change6', 'deMarker_change7', 'deMarker_change8', 'deMarker_change9',
               'deMarker_change10',
               'deMarker_current_change1', 'deMarker_current_change2', 'deMarker_current_change3',
               'deMarker_current_change4',
               'deMarker_current_change5',
               'deMarker_current_change6', 'deMarker_current_change7', 'deMarker_current_change8',
               'deMarker_current_change9',
               'deMarker_current_change10',
               'envelopes_upper_value', 'envelopes_lower_value',
               'force',
               'force_change1', 'force_change2', 'force_change3', 'force_change4', 'force_change5',
               'force_change6', 'force_change7', 'force_change8', 'force_change9',
               'force_change10',
               'force_current_change1', 'force_current_change2', 'force_current_change3',
               'force_current_change4',
               'force_current_change5',
               'force_current_change6', 'force_current_change7', 'force_current_change8',
               'force_current_change9',
               'force_current_change10',
               'fractals_up_arrow', 'fractals_down_arrow',
               'frAMA',
               'frAMA_change1', 'frAMA_change2', 'frAMA_change3', 'frAMA_change4', 'frAMA_change5',
               'frAMA_change6', 'frAMA_change7', 'frAMA_change8', 'frAMA_change9',
               'frAMA_change10',
               'frAMA_current_change1', 'frAMA_current_change2', 'frAMA_current_change3',
               'frAMA_current_change4',
               'frAMA_current_change5',
               'frAMA_current_change6', 'frAMA_current_change7', 'frAMA_current_change8',
               'frAMA_current_change9',
               'frAMA_current_change10',
               'gator_ups', 'gator_up_color', 'gator_downs', 'gator_downs_color',
               'tenkan_sen', 'kijun_sen', 'senkou_span_A', 'senkou_span_B', 'chinkou_span',
               'bwmfi_value', 'bwmfi_color',
               'bwmfi_change1', 'bwmfi_change2', 'bwmfi_change3', 'bwmfi_change4', 'bwmfi_change5',
               'bwmfi_change6', 'bwmfi_change7', 'bwmfi_change8', 'bwmfi_change9',
               'bwmfi_change10',
               'bwmfi_current_change1', 'bwmfi_current_change2', 'bwmfi_current_change3',
               'bwmfi_current_change4',
               'bwmfi_current_change5',
               'bwmfi_current_change6', 'bwmfi_current_change7', 'bwmfi_current_change8',
               'bwmfi_current_change9',
               'bwmfi_current_change10',
               'momentum',
               'momentum_change1', 'momentum_change2', 'momentum_change3', 'momentum_change4', 'momentum_change5',
               'momentum_change6', 'momentum_change7', 'momentum_change8', 'momentum_change9',
               'momentum_change10',
               'momentum_current_change1', 'momentum_current_change2', 'momentum_current_change3',
               'momentum_current_change4',
               'momentum_current_change5',
               'momentum_current_change6', 'momentum_current_change7', 'momentum_current_change8',
               'momentum_current_change9',
               'momentum_current_change10',
               'mfi',
               'mfi_change1', 'mfi_change2', 'mfi_change3', 'mfi_change4', 'mfi_change5',
               'mfi_change6', 'mfi_change7', 'mfi_change8', 'mfi_change9',
               'mfi_change10',
               'mfi_current_change1', 'mfi_current_change2', 'mfi_current_change3',
               'mfi_current_change4',
               'mfi_current_change5',
               'mfi_current_change6', 'mfi_current_change7', 'mfi_current_change8',
               'mfi_current_change9',
               'mfi_current_change10',
               'osMA',
               'osMA_change1', 'osMA_change2', 'osMA_change3', 'osMA_change4', 'osMA_change5',
               'osMA_change6', 'osMA_change7', 'osMA_change8', 'osMA_change9',
               'osMA_change10',
               'osMA_current_change1', 'osMA_current_change2', 'osMA_current_change3',
               'osMA_current_change4',
               'osMA_current_change5',
               'osMA_current_change6', 'osMA_current_change7', 'osMA_current_change8',
               'osMA_current_change9',
               'osMA_current_change10',
               'obv',
               'obv_change1', 'obv_change2', 'obv_change3', 'obv_change4', 'obv_change5',
               'obv_change6', 'obv_change7', 'obv_change8', 'obv_change9',
               'obv_change10',
               'obv_current_change1', 'obv_current_change2', 'obv_current_change3',
               'obv_current_change4',
               'obv_current_change5',
               'obv_current_change6', 'obv_current_change7', 'obv_current_change8',
               'obv_current_change9',
               'obv_current_change10',
               'rvi', 'rvi_signal',
               'rvi_change1', 'rvi_change2', 'rvi_change3', 'rvi_change4', 'rvi_change5',
               'rvi_change6', 'rvi_change7', 'rvi_change8', 'rvi_change9',
               'rvi_change10',
               'rvi_current_change1', 'rvi_current_change2', 'rvi_current_change3',
               'rvi_current_change4',
               'rvi_current_change5',
               'rvi_current_change6', 'rvi_current_change7', 'rvi_current_change8',
               'rvi_current_change9',
               'rvi_current_change10',
               'stdDev',
               'stdDev_change1', 'stdDev_change2', 'stdDev_change3', 'stdDev_change4', 'stdDev_change5',
               'stdDev_change6', 'stdDev_change7', 'stdDev_change8', 'stdDev_change9',
               'stdDev_change10',
               'stdDev_current_change1', 'stdDev_current_change2', 'stdDev_current_change3',
               'stdDev_current_change4',
               'stdDev_current_change5',
               'stdDev_current_change6', 'stdDev_current_change7', 'stdDev_current_change8',
               'stdDev_current_change9',
               'stdDev_current_change10',
               'tema',
               'tema_change1', 'tema_change2', 'tema_change3', 'tema_change4', 'tema_change5',
               'tema_change6', 'tema_change7', 'tema_change8', 'tema_change9',
               'tema_change10',
               'tema_current_change1', 'tema_current_change2', 'tema_current_change3',
               'tema_current_change4',
               'tema_current_change5',
               'tema_current_change6', 'tema_current_change7', 'tema_current_change8',
               'tema_current_change9',
               'tema_current_change10',
               'triX',
               'triX_change1', 'triX_change2', 'triX_change3', 'triX_change4', 'triX_change5',
               'triX_change6', 'triX_change7', 'triX_change8', 'triX_change9',
               'triX_change10',
               'triX_current_change1', 'triX_current_change2', 'triX_current_change3',
               'triX_current_change4',
               'triX_current_change5',
               'triX_current_change6', 'triX_current_change7', 'triX_current_change8',
               'triX_current_change9',
               'triX_current_change10',
               'wpr',
               'wpr_change1', 'wpr_change2', 'wpr_change3', 'wpr_change4', 'wpr_change5',
               'wpr_change6', 'wpr_change7', 'wpr_change8', 'wpr_change9',
               'wpr_change10',
               'wpr_current_change1', 'wpr_current_change2', 'wpr_current_change3',
               'wpr_current_change4',
               'wpr_current_change5',
               'wpr_current_change6', 'wpr_current_change7', 'wpr_current_change8',
               'wpr_current_change9',
               'wpr_current_change10',
               'vidya',
               'vidya_change1', 'vidya_change2', 'vidya_change3', 'vidya_change4', 'vidya_change5',
               'vidya_change6', 'vidya_change7', 'vidya_change8', 'vidya_change9',
               'vidya_change10',
               'vidya_current_change1', 'vidya_current_change2', 'vidya_current_change3',
               'vidya_current_change4',
               'vidya_current_change5',
               'vidya_current_change6', 'vidya_current_change7', 'vidya_current_change8',
               'vidya_current_change9',
               'vidya_current_change10',
               'atr_5_10_type',
               'macd_type',
               'sma_5_10_type',
               'ema_5_10_type',
               'smma_5_10_type',
               'lwma_5_10_type',
               'rsi_5_14_type',
               'sar_type',
               'adx_type',
               'cci_type',
               'stoch_type',
               'boll_type',
               'ac_type',
               'ad_type',
               'adxWilder_type',
               'alligator_type',
               'ama_type',
               'ao_type',
               'bearsPower_type',
               'bullsPower_type',
               'chaikin_type',
               'dema_type',
               'deMarker_type',
               'envelopes_type',
               'force_type',
               'fractals_type',
               'frAMA_type',
               'gator_type',
               'ichimoku_type',
               'bwmfi_type',
               'momentum_type',
               'mfi_type',
               'osMA_type',
               'obv_type',
               'rvi_type',
               'stdDev_type',
               'tema_type',
               'triX_type',
               'wpr_type',
               'vidya_type',
               'atr5_changeValue1', 'atr5_changeValue2', 'atr5_changeValue3', 'atr5_changeValue4',
               'atr5_changeValue5', 'atr5_changeValue6', 'atr5_changeValue7', 'atr5_changeValue8',
               'atr5_changeValue9', 'atr5_changeValue10',
               'atr10_changeValue1', 'atr10_changeValue2', 'atr10_changeValue3', 'atr10_changeValue4',
               'atr10_changeValue5', 'atr10_changeValue6', 'atr10_changeValue7', 'atr10_changeValue8',
               'atr10_changeValue9', 'atr10_changeValue10',
               'macd_changeValue1', 'macd_changeValue2', 'macd_changeValue3', 'macd_changeValue4',
               'macd_changeValue5', 'macd_changeValue6', 'macd_changeValue7', 'macd_changeValue8',
               'macd_changeValue9', 'macd_changeValue10',
               'sma5_changeValue1', 'sma5_changeValue2', 'sma5_changeValue3', 'sma5_changeValue4',
               'sma5_changeValue5', 'sma5_changeValue6', 'sma5_changeValue7', 'sma5_changeValue8',
               'sma5_changeValue9', 'sma5_changeValue10',
               'sma10_changeValue1', 'sma10_changeValue2', 'sma10_changeValue3', 'sma10_changeValue4',
               'sma10_changeValue5', 'sma10_changeValue6', 'sma10_changeValue7', 'sma10_changeValue8',
               'sma10_changeValue9', 'sma10_changeValue10',
               'rsi5_changeValue1', 'rsi5_changeValue2', 'rsi5_changeValue3', 'rsi5_changeValue4',
               'rsi5_changeValue5', 'rsi5_changeValue6', 'rsi5_changeValue7', 'rsi5_changeValue8',
               'rsi5_changeValue9', 'rsi5_changeValue10',
               'rsi14_changeValue1', 'rsi14_changeValue2', 'rsi14_changeValue3', 'rsi14_changeValue4',
               'rsi14_changeValue5', 'rsi14_changeValue6', 'rsi14_changeValue7', 'rsi14_changeValue8',
               'rsi14_changeValue9', 'rsi14_changeValue10',
               'sar_changeValue1', 'sar_changeValue2', 'sar_changeValue3', 'sar_changeValue4',
               'sar_changeValue5', 'sar_changeValue6', 'sar_changeValue7', 'sar_changeValue8',
               'sar_changeValue9', 'sar_changeValue10',
               'adx_changeValue1', 'adx_changeValue2', 'adx_changeValue3', 'adx_changeValue4',
               'adx_changeValue5', 'adx_changeValue6', 'adx_changeValue7', 'adx_changeValue8',
               'adx_changeValue9', 'adx_changeValue10',
               'cci_changeValue1', 'cci_changeValue2', 'cci_changeValue3', 'cci_changeValue4',
               'cci_changeValue5', 'cci_changeValue6', 'cci_changeValue7', 'cci_changeValue8',
               'cci_changeValue9', 'cci_changeValue10',
               'slowk_changeValue1', 'slowk_changeValue2', 'slowk_changeValue3', 'slowk_changeValue4',
               'slowk_changeValue5', 'slowk_changeValue6', 'slowk_changeValue7', 'slowk_changeValue8',
               'slowk_changeValue9', 'slowk_changeValue10',
               'ac_changeValue1', 'ac_changeValue2', 'ac_changeValue3', 'ac_changeValue4',
               'ac_changeValue5', 'ac_changeValue6', 'ac_changeValue7', 'ac_changeValue8',
               'ac_changeValue9', 'ac_changeValue10',
               'adxWilder_changeValue1', 'adxWilder_changeValue2', 'adxWilder_changeValue3',
               'adxWilder_changeValue4',
               'adxWilder_changeValue5', 'adxWilder_changeValue6', 'adxWilder_changeValue7',
               'adxWilder_changeValue8',
               'adxWilder_changeValue9', 'adxWilder_changeValue10',
               'lips_changeValue1', 'lips_changeValue2', 'lips_changeValue3', 'lips_changeValue4',
               'lips_changeValue5', 'lips_changeValue6', 'lips_changeValue7', 'lips_changeValue8',
               'lips_changeValue9', 'lips_changeValue10',
               'ama_changeValue1', 'ama_changeValue2', 'ama_changeValue3', 'ama_changeValue4',
               'ama_changeValue5', 'ama_changeValue6', 'ama_changeValue7', 'ama_changeValue8',
               'ama_changeValue9', 'ama_changeValue10',
               'ao_changeValue1', 'ao_changeValue2', 'ao_changeValue3', 'ao_changeValue4',
               'ao_changeValue5', 'ao_changeValue6', 'ao_changeValue7', 'ao_changeValue8',
               'ao_changeValue9', 'ao_changeValue10',
               'bears_changeValue1', 'bears_changeValue2', 'bears_changeValue3', 'bears_changeValue4',
               'bears_changeValue5', 'bears_changeValue6', 'bears_changeValue7', 'bears_changeValue8',
               'bears_changeValue9', 'bears_changeValue10',
               'bulls_changeValue1', 'bulls_changeValue2', 'bulls_changeValue3', 'bulls_changeValue4',
               'bulls_changeValue5', 'bulls_changeValue6', 'bulls_changeValue7', 'bulls_changeValue8',
               'bulls_changeValue9', 'bulls_changeValue10',
               'chaikin_changeValue1', 'chaikin_changeValue2', 'chaikin_changeValue3', 'chaikin_changeValue4',
               'chaikin_changeValue5', 'chaikin_changeValue6', 'chaikin_changeValue7', 'chaikin_changeValue8',
               'chaikin_changeValue9', 'chaikin_changeValue10',
               'deMarker_changeValue1', 'deMarker_changeValue2', 'deMarker_changeValue3', 'deMarker_changeValue4',
               'deMarker_changeValue5', 'deMarker_changeValue6', 'deMarker_changeValue7', 'deMarker_changeValue8',
               'deMarker_changeValue9', 'deMarker_changeValue10',
               'force_changeValue1', 'force_changeValue2', 'force_changeValue3', 'force_changeValue4',
               'force_changeValue5', 'force_changeValue6', 'force_changeValue7', 'force_changeValue8',
               'force_changeValue9', 'force_changeValue10',
               'bwmfi_changeValue1', 'bwmfi_changeValue2', 'bwmfi_changeValue3', 'bwmfi_changeValue4',
               'bwmfi_changeValue5', 'bwmfi_changeValue6', 'bwmfi_changeValue7', 'bwmfi_changeValue8',
               'bwmfi_changeValue9', 'bwmfi_changeValue10',
               'momentum_changeValue1', 'momentum_changeValue2', 'momentum_changeValue3', 'momentum_changeValue4',
               'momentum_changeValue5', 'momentum_changeValue6', 'momentum_changeValue7', 'momentum_changeValue8',
               'momentum_changeValue9', 'momentum_changeValue10',
               'mfi_changeValue1', 'mfi_changeValue2', 'mfi_changeValue3', 'mfi_changeValue4',
               'mfi_changeValue5', 'mfi_changeValue6', 'mfi_changeValue7', 'mfi_changeValue8',
               'mfi_changeValue9', 'mfi_changeValue10',
               'osMA_changeValue1', 'osMA_changeValue2', 'osMA_changeValue3', 'osMA_changeValue4',
               'osMA_changeValue5', 'osMA_changeValue6', 'osMA_changeValue7', 'osMA_changeValue8',
               'osMA_changeValue9', 'osMA_changeValue10',
               'rvi_changeValue1', 'rvi_changeValue2', 'rvi_changeValue3', 'rvi_changeValue4',
               'rvi_changeValue5', 'rvi_changeValue6', 'rvi_changeValue7', 'rvi_changeValue8',
               'rvi_changeValue9', 'rvi_changeValue10',
               'stdDev_changeValue1', 'stdDev_changeValue2', 'stdDev_changeValue3', 'stdDev_changeValue4',
               'stdDev_changeValue5', 'stdDev_changeValue6', 'stdDev_changeValue7', 'stdDev_changeValue8',
               'stdDev_changeValue9', 'stdDev_changeValue10',
               'wpr_changeValue1', 'wpr_changeValue2', 'wpr_changeValue3', 'wpr_changeValue4',
               'wpr_changeValue5', 'wpr_changeValue6', 'wpr_changeValue7', 'wpr_changeValue8',
               'wpr_changeValue9', 'wpr_changeValue10',
               'his_interval', 'interval_10', 'interval_20', 'interval_30'
               ]
    clm_l = [ i + '_' + binary_file.split('/')[-1] for i in clm]
    # 转为DataFrame 并添加列名
    data = pd.DataFrame(data_list,columns=clm_l)

    # print('ac_color\n',type(data['ac_color'][1]))
    print("DataFrame转换完成！", binary_file)
    print("数据长度",len(data),"数据维度",len(data_format))
    print('bin_to_data\n',data[:3])

    return data