import akshare as ak
from src.utils.DBUtils import *
import sys

print(sys.path)
# import numpy
# import talib
#
# close = numpy.random.random(100)
# output = talib.SMA(close)

# stock_em_hsgt_industry_rank_df = ak.stock_em_hsgt_board_rank(symbol="北向资金增持行业板块排行", indicator="今日")
# print(stock_em_hsgt_industry_rank_df)

class Collect(object):
    dbUtils = DBUtils()

    def init(self):
        self.dbUtils.init()
        self.initCode()

    def initCode(self):
        stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
        for index in stock_zh_a_spot_em_df.index:
            value = stock_zh_a_spot_em_df.loc[index]
            code = value.values[1]
            name = value.values[2]
            sele = """
                select 
            """
            # print(code + name)


coll = Collect()
coll.init()

#  获取所有股票代码
# stock_info_a_code_name_df = ak.stock_info_a_code_name()
# ss = set()
# count = 0
# for index in stock_info_a_code_name_df.index:
#     value = stock_info_a_code_name_df.loc[index]
#     code = value.values[0]
#     name = value.values[1]
#     print(name)
#     ss.add(code[:3])
#     count = count + 1
#
# print(count)
# print(ss)
