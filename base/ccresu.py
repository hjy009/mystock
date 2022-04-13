import numpy as np
import pandas as pd
from sklearn import svm
import datetime
from base import ev_resu,ccmid
from datasets import trade_cal,ccdy

class ccresu():
    dys = {}

    def keyvalue(self,ts_code):
        if ts_code not in self.dys:
            self.dys[ts_code] = ev_resu.ev_resu(stock_code=ts_code)
            self.dys[ts_code].load_file()
        res = self.dys[ts_code]
        return res

    def df_stock(self,ts_code):
        if ts_code not in self.dys:
            self.keyvalue(ts_code)
        df = self.keyvalue(ts_code).data
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

    def set_f1(self,stock,from_date,to_date,predict_window):
        # 计算查全率
        resu_real = 'resu_real'
        resu_predict = str(predict_window)

        df = ccmid.i.df_stdate(stock, from_date, to_date)
        recall_son = len(df.loc[(df[resu_real] == 1) & (df[resu_predict] == 1)])
        recall_mon = len(df.loc[(df[resu_real] == 1)])
        if recall_mon ==0:
            recall = 0
        else:
            recall = recall_son / recall_mon
        # 计算查准率
        acc_son = len(df.loc[(df[resu_real] == 1) & (df[resu_predict] == 1)])
        acc_mon = len(df.loc[(df[resu_predict] == 1)])
        if acc_mon == 0:
            acc = recall = acc_neg = f1 = 0
        else:
            acc = acc_son / acc_mon
        # 计算查准率(负样本)
        acc_neg_son = len(df.loc[(df[resu_real] == 0) & (df[resu_predict] == 0)])
        acc_neg_mon = len(df.loc[(df[resu_predict] == 0)])
        if acc_neg_mon == 0:
            acc_neg_mon = -1
            acc_neg = -1
        else:
            acc_neg = acc_neg_son / acc_neg_mon
        # 计算 F1 分值
        if acc + recall == 0:
            acc = recall = acc_neg = f1 = 0
        else:
            f1 = (2 * acc * recall) / (acc + recall)
        if len(df)==0:
            predict = 0
        else:
            predict = int(df[resu_predict].iloc[-1])
        # 将评估结果存入结果表model_ev_resu中

        er = self.keyvalue(stock)
        dic = dict(zip(er.data.columns, [to_date, stock, acc, recall, f1, acc_neg, 'svm', str(predict)]))
        er.append_dict(dic)
        er.save()
        print(str(stock) + to_date + '   Precision : ' + str(acc) + '   Recall : ' + str(recall) + '   F1 : ' + str(
            f1) + '   Acc_Neg : ' + str(acc_neg))
        return dic

    def set_fs(self,stock,from_date,to_date,f1_window,predict_window):
        # 建评估时间序列, para_window参数代表回测窗口长度
        #fs_seq = trade_cal.date_range(from_date=from_date, to_date=to_date, is_open=1)
        df = ccmid.i.df_stdate(stock,from_date,to_date)
        fs_seq = df['trade_date'].astype(int).astype(str)
        for d in fs_seq:
            # 每日推进式建模，并获取对下一个交易日的预测结果
            dt = str(d)
            date_start = (
                        datetime.datetime.strptime(dt, '%Y%m%d') -
                        datetime.timedelta(days=f1_window)).strftime('%Y%m%d')
            date_end = dt
            f1_seq = trade_cal.date_range(date_start, date_end, 1).astype(str)
            date_start = f1_seq[0]
            date_end = f1_seq[-1]
            self.set_f1(stock, date_start, date_end, predict_window)

        return

i = ccresu()