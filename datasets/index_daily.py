"""

指数日线行情

接口：index_daily
描述：获取指数每日行情，还可以通过bar接口获取。由于服务器压力，目前规则是单次调取最多取8000行记录，可以设置start和end日期补全。指数行情也可以通过通用行情接口获取数据．
权限：常规指数需累积200积分可低频调取，5000积分以上正常调取无限制。本接口不包括申万行情数据，申万等行业指数行情请在QQ群联系群主，具体请参阅积分获取办法

输入参数
名称 	类型 	必选 	描述
ts_code 	str 	Y 	指数代码
trade_date 	str 	N 	交易日期 （日期格式：YYYYMMDD，下同）
start_date 	str 	N 	开始日期
end_date 	None 	N 	结束日期

输出参数
名称 	类型 	描述
ts_code 	str 	TS指数代码
trade_date 	str 	交易日
close 	float 	收盘点位
open 	float 	开盘点位
high 	float 	最高点位
low 	float 	最低点位
pre_close 	float 	昨日收盘点
change 	float 	涨跌点
pct_chg 	float 	涨跌幅（%）
vol 	float 	成交量（手）
amount 	float 	成交额（千元）

接口使用


pro = ts.pro_api()

df = pro.index_daily(ts_code='399300.SZ')

#或者按日期取

df = pro.index_daily(ts_code='399300.SZ', start_date='20180101', end_date='20181010')

数据样例

        ts_code trade_date      close       open       high        low  \
0     399300.SZ   20180903  3321.8248  3320.6898  3325.6070  3291.7842
1     399300.SZ   20180831  3334.5036  3333.3801  3356.5757  3310.8726
2     399300.SZ   20180830  3351.0942  3385.8052  3402.5626  3349.4688
3     399300.SZ   20180829  3386.5736  3393.0527  3398.7139  3377.1231
4     399300.SZ   20180828  3400.1705  3408.1502  3416.5929  3388.8143
5     399300.SZ   20180827  3406.5735  3339.3894  3406.5735  3339.2646
6     399300.SZ   20180824  3325.3347  3308.4778  3353.0445  3291.8654
7     399300.SZ   20180823  3320.0257  3308.4589  3336.1123  3285.8141
8     399300.SZ   20180822  3307.9545  3328.9693  3328.9693  3299.3938
9     399300.SZ   20180821  3326.6489  3271.8402  3331.7077  3270.0302
10    399300.SZ   20180820  3267.2498  3238.2150  3267.2498  3209.0115
11    399300.SZ   20180817  3229.6198  3305.8954  3311.5729  3224.0999
12    399300.SZ   20180816  3276.7276  3251.8556  3315.2031  3231.5561
13    399300.SZ   20180815  3291.9760  3371.9590  3372.1369  3288.7088
14    399300.SZ   20180814  3372.9137  3386.4832  3391.7290  3356.6142
15    399300.SZ   20180813  3390.3441  3369.9812  3396.1883  3336.6956
16    399300.SZ   20180810  3405.0191  3398.4139  3424.0411  3380.5731

"""
from datasets import trade_cal, paths
import pandas as pd
import time

class index_daily(trade_cal.trade_cal):
    ts_code = '000001.SH'

    def __init__(self,ts_code='000001.SH',api_name = ''):
        self.ts_code = ts_code
        super(index_daily, self).__init__(api_name)
        self.ord_add = 'des'
        self.ftime_name = 'trade_date'
        return

    def get_filepath(self):
        res = paths.pathapi2(self.api_name,self.ts_code)
        return res

    def info_key(self):
        res = self.api_name+'.'+self.ts_code
        return res

    def api_query(self):
        k5 = trade_cal.i.k5(start=time.strftime("%Y%m%d", self.stdate),
                            end=time.strftime("%Y%m%d", self.eddate))
        df = pd.DataFrame()
        for dts in k5:
            df = self.pro.index_daily(
                                ts_code=self.ts_code,
                                start_date=dts[0],
                                end_date=dts[1]).append(other=df,ignore_index=True)
            self.sleep()
        return df


