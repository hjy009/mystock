import numpy as np
import pandas as pd
from sklearn import svm
import datetime
from base import ev_mid,dcds
from datasets import trade_cal,ccdy

class ccmid():
    dys = {}

    def keyvalue(self,ts_code):
        if ts_code not in self.dys:
            self.dys[ts_code] = ev_mid.ev_mid(stock_code=ts_code)
            self.dys[ts_code].load_file()
        res = self.dys[ts_code]
        return res

    def df_stock(self,ts_code):
        if ts_code not in self.dys:
            df = self.keyvalue(ts_code).data
        else:
            df = self.dys[ts_code].data
        return df

    def df_stdate(self,ts_code,from_date,to_date):
        df = self.df_stock(ts_code)
        ftime_name = 'trade_date'
        df = df.loc[(df[ftime_name].astype(str) >= from_date) & (df[ftime_name].astype(str) <= to_date)]
        return df

    def valuebykey(self,ts_code,st_date,key):
        df = self.df_stdate(ts_code,st_date,st_date)
        if (key not in df.columns) | (len(df)==0):
            res = np.nan
        else:
            res = df[key].iloc[0]
        return  res

    def set_predict(self,stock,state_dt,para_window):
        # 建评估时间序列, para_window参数代表回测窗口长度
        date_start = (
                    datetime.datetime.strptime(state_dt, '%Y%m%d') -
                    datetime.timedelta(days=para_window)
                    ).strftime('%Y%m%d')
        date_end = state_dt
        dc = dcds.i
        dc.collectDATA(stock, date_start, date_end)
        model = svm.SVC()  # 建模
        model.fit(dc.data_train, dc.data_target)  # 训练
        ans2 = model.predict(dc.test_case)  # 预测
        em = self.keyvalue(stock)
        dic = {}
        dic['trade_date'] = state_dt
        dic['stock_code'] = stock
        sl = str(para_window)
        dic[sl] = ans2[0]
        em.append_dict(dic)
        em.save()
        return ans2[0]

    def set_pds(self,stock,from_date,to_date,para_window):
        # 建评估时间序列, para_window参数代表回测窗口长度
        date_seq = trade_cal.date_range(from_date=from_date, to_date=to_date, is_open=1)
        for d in date_seq:
            dt = str(d)
            if np.isnan(self.valuebykey(stock, dt, str(para_window))):
                self.set_predict(stock, dt, para_window)

        return

    def set_reals(self,stock,from_date,to_date):
        resu_real = 'resu_real'
        df = ccdy.i.df_stdate(stock, from_date, to_date)
        tg = pd.DataFrame()
        tg['1'] = df['close'][0:len(df) - 1].values
        tg['2'] = df['close'][1:len(df)].values
        tg = tg['1'] < tg['2']
        tg[tg == True] = 1
        df1 = pd.DataFrame(data=tg)
        df1.index = df.index[0:len(df.index) - 1]
        df1.columns = [resu_real]
        em = self.dys[stock]
        em.data = df1.combine_first(em.data)
        em.save()
        return

i = ccmid()