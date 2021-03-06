"""

日线行情

接口：daily
数据说明：交易日每天15点～16点之间。本接口是未复权行情，停牌期间不提供数据。
调取说明：基础积分每分钟内最多调取200次，每次4000条数据，相当于超过18年历史，用户获得超过5000积分无频次限制。
描述：获取股票行情数据，或通过通用行情接口获取数据，包含了前后复权数据。

输入参数
名称     类型     必选     描述
ts_code     str     N     股票代码（二选一）
trade_date     str     N     交易日期（二选一）
start_date     str     N     开始日期(YYYYMMDD)
end_date     str     N     结束日期(YYYYMMDD)

注：日期都填YYYYMMDD格式，比如20181010

输出参数
名称     类型     描述
ts_code     str     股票代码
trade_date     str     交易日期
open     float     开盘价
high     float     最高价
low     float     最低价
close     float     收盘价
pre_close     float     昨收价
change     float     涨跌额
pct_chg     float     涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
vol     float     成交量 （手）
amount     float     成交额 （千元）

接口示例


pro = ts.pro_api()

df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')

或者


df = pro.query('daily', ts_code='000001.SZ', start_date='20180701', end_date='20180718')

也可以通过日期取历史某一天的全部历史


df = pro.daily(trade_date='20180810')

数据样例

 ts_code trade_date  open  high   low  close  pre_close  change    pct_chg  vol        amount
0  000001.SZ   20180718  8.75  8.85  8.69   8.70       8.72   -0.02       -0.23   525152.77   460697.377
1  000001.SZ   20180717  8.74  8.75  8.66   8.72       8.73   -0.01       -0.11   375356.33   326396.994
2  000001.SZ   20180716  8.85  8.90  8.69   8.73       8.88   -0.15       -1.69   689845.58   603427.713
3  000001.SZ   20180713  8.92  8.94  8.82   8.88       8.88    0.00        0.00   603378.21   535401.175
4  000001.SZ   20180712  8.60  8.97  8.58   8.88       8.64    0.24        2.78  1140492.31  1008658.828
5  000001.SZ   20180711  8.76  8.83  8.68   8.78       8.98   -0.20       -2.23   851296.70   744765.824
6  000001.SZ   20180710  9.02  9.02  8.89   8.98       9.03   -0.05       -0.55   896862.02   803038.965
7  000001.SZ   20180709  8.69  9.03  8.68   9.03       8.66    0.37        4.27  1409954.60  1255007.609
8  000001.SZ   20180706  8.61  8.78  8.45   8.66       8.60    0.06        0.70   988282.69   852071.526
9  000001.SZ   20180705  8.62  8.73  8.55   8.60       8.61   -0.01       -0.12   835768.77   722169.579



"""
from datasets import trade_cal, paths
import pandas as pd
import time

class daily(trade_cal.trade_cal):
    ts_code = '0000001.SZ'

    def __init__(self,ts_code='000001.SZ',api_name = 'daily'):
        self.ts_code = ts_code
        super(daily, self).__init__(api_name)
        self.ord_add = 'idx'
        self.ftime_name = 'trade_date'
        return

    def get_filepath(self):
        #res = paths.pathapi2(self.api_name,self.ts_code)
        res = paths.get_dailypath(self.ts_code)
        return res

    def info_key(self):
        res = self.api_name+'.'+self.ts_code
        return res

    def api_query(self):
        k5 = trade_cal.i.k5(start=time.strftime("%Y%m%d", self.stdate),
                            end=time.strftime("%Y%m%d", self.eddate))
        df = pd.DataFrame()
        for dts in k5:
            df = self.pro.query('daily',
                                ts_code=self.ts_code,
                                start_date=dts[0],
                                end_date=dts[1]).append(other=df,ignore_index=True)
            self.sleep()
        if len(df)>0:
            df.index = df[self.ftime_name].astype('datetime64')
        return df


