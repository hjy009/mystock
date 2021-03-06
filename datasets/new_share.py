"""


IPO新股列表

接口：new_share
描述：获取新股上市列表数据
限量：单次最大2000条，总量不限制
积分：用户需要至少120积分才可以调取，具体请参阅积分获取办法

输入参数
名称     类型     必选     描述
start_date     str     N     上网发行开始日期
end_date     str     N     上网发行结束日期

输出参数
名称     类型     默认显示     描述
ts_code     str     Y     TS股票代码
sub_code     str     Y     申购代码
name     str     Y     名称
ipo_date     str     Y     上网发行日期
issue_date     str     Y     上市日期
amount     float     Y     发行总量（万股）
market_amount     float     Y     上网发行总量（万股）
price     float     Y     发行价格
pe     float     Y     市盈率
limit_amount     float     Y     个人申购上限（万股）
funds     float     Y     募集资金（亿元）
ballot     float     Y     中签率

接口示例


pro = ts.pro_api()

df = pro.new_share(start_date='20180901', end_date='20181018')

数据示例

  ts_code       sub_code  name  ipo_date    issue_date   amount  market_amount  \
0   002939.SZ   002939  长城证券  20181017       None  31034.0        27931.0   
1   002940.SZ   002940   昂利康  20181011   20181023   2250.0         2025.0   
2   601162.SH   780162  天风证券  20181009   20181019  51800.0        46620.0   
3   300694.SZ   300694  蠡湖股份  20180927   20181015   5383.0         4845.0   
4   300760.SZ   300760  迈瑞医疗  20180927   20181016  12160.0        10944.0   
5   300749.SZ   300749  顶固集创  20180913   20180925   2850.0         2565.0   
6   002937.SZ   002937  兴瑞科技  20180912   20180926   4600.0         4140.0   
7   601577.SH   780577  长沙银行  20180912   20180926  34216.0        30794.0   
8   603583.SH   732583  捷昌驱动  20180911   20180921   3020.0         2718.0   
9   002936.SZ   002936  郑州银行  20180907   20180919  60000.0        54000.0   
10  300748.SZ   300748  金力永磁  20180906   20180921   4160.0         3744.0   
11  603810.SH   732810  丰山集团  20180906   20180917   2000.0         2000.0   
12  002938.SZ   002938  鹏鼎控股  20180905   20180918  23114.0        20803.0   

    price     pe  limit_amount   funds  ballot  
0    6.31  22.98          9.30  19.582    0.16  
1   23.07  22.99          0.90   5.191    0.03  
2    1.79  22.86         15.50   0.000    0.25  
3    9.89  22.98          2.15   5.324    0.04  
4   48.80  22.99          3.60  59.341    0.08  
5   12.22  22.99          1.10   3.483    0.03  
6    9.94  22.99          1.80   4.572    0.04  
7    7.99   6.97         10.20  27.338    0.17  
8   29.17  22.99          1.20   8.809    0.03  
9    4.59   6.50         18.00  27.540    0.25  
10   5.39  22.98          1.20   2.242    0.05  
11  25.43  20.39          2.00   5.086    0.02  
12  16.07  22.99          6.90  37.145    0.12  


"""
import tushare as ts
from datasets import stock_basic
from datetime import date
from datetime import timedelta

class new_share(stock_basic.stock_basic):
    
    def __init__(self,api_name = 'new_share'):
        self.init(api_name)
        return
    
    def api_query(self):
        pro = ts.pro_api()
        dt = date.today()
        dt1 = dt + timedelta(days=30)
        df = pro.new_share(start_date=dt.strftime('%Y%m%d'), end_date=dt1.strftime('%Y%m%d'))
        return df
