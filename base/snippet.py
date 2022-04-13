import gc
import tushare as ts
from datasets import infomations,infomation,tusets, stock_basic, trade_cal, new_share, pro_bar, daily, dailys, adj_factor
from datasets import cachedy,ccdy
from datasets import index_basic,cacheidx
from base import  dfinfo
import time
import numpy as np
import pandas as pd


print(ts.__version__)

#ts = tusets.tusets()
#ts.save_fdate()

#info = infomation.infomation()
#info.init()
stock_basic.i.init()
#stb.save_fdate()

trade_cal.i.init()
#tdc.save_fdate()
#trade_cal.i.k5(start='19901209',end='20210118')

#dy = daily.daily()
#dy.init()
#daily.save_all()
#dy.save_fdate()
#dys = dailys.dailys()
#dys.init()
#dys.save_fdate()

chd = cachedy.cachedy()
chd.init()
#dailys 文件太大
#chd.save_dailys()
chd.save_dailyx()

#chd.save_all_fdate()
#chd.save_all_ltdate()
#chd.save_allx()

#cidx = cacheidx.cacheidx()
#cidx.save_ltdate(market='SSE')
#cidx.save_ltdate(market='SZSE')

#nsh = new_share.load_data()
#dts = daily.load_data('000001.SZ')

#tst = tusets.tusets()
#tst.stb.init()
#tst.tdc.init()
#tst.stc_save_all()


#stock_code.stock_code(api_name = 'daily',ts_code='000001.SZ')
#stock_code.save_all()
#pro_bar.save_all()
#daily.save_all()
#adj_factor.save_all()
#dt = date.today()
#daily.save_date(dt.strftime('%Y%m%d'))
#daily.save_date('20191128')

#pro_bar.save_all()

#pro = ts.pro_api()

#df1 = pro.daily(trade_date='20180810')

#df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')

# np.savez(self.file_path,values=df.values,columns=df.columns,infomation=self.info)
# self.data = np.load(self.file_path, allow_pickle=True)

#dy = ccdy.i.df_stock(ts_code='000001.SZ')
#df = ccdy.i.df_stdate(ts_code='000002.SZ',from_date='20210108',to_date='20210108')
#close = ccdy.i.valuebykey(ts_code='000002.SZ',st_date='20210108',key='close')

#idxb = index_basic.i
#idxb.init()


#单线程，需要单独保存
infomations.i.save_file()
gc.collect()



