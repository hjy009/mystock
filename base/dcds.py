# -*- coding:utf8 -*-
import numpy as np
import pandas as pd
from base import model_daily
from datasets import ccdy


class dcds(model_daily.model_daily):

    def __init__(self, api_name='dcds'):
        super(dcds, self).__init__(api_name)
        return

    def collectDATA(self,in_code,from_dt,to_dt):
        self.stock_code = in_code
        self.from_dt = from_dt
        self.to_dt = to_dt
        # 获取日线基础行情(开盘价，收盘价，最高价，最低价，成交量，成交额)
        df = ccdy.i.df_stdate(ts_code=in_code,from_date=from_dt,to_date=to_dt)
        self.date_seq = df['trade_date']
        self.open_list = df['open']
        self.close_list = df['close']
        self.high_list = df['high']
        self.low_list = df['low']
        self.vol_list = df['vol']
        self.amount_list = df['amount']
        #df = self.data.loc[(self.date_seq.astype(str) >= self.from_dt) & (self.date_seq.astype(str) <= self.to_dt)].sort_index(ascending=False)

        # 将日线行情整合为训练集(其中self.train是输入集，self.target是输出集，self.test_case是end_dt那天的单条测试输入)
        self.data_train = []
        self.data_target = []
        self.data_target_onehot = []
        self.cnt_pos = 0
        self.test_case = []
        #self.data_train = df[['open','close','high','low','vol','amount']][0:len(df)-1].values
        for i in range(1,len(df)):
            train = [self.open_list[i-1],self.close_list[i-1],self.high_list[i-1],self.low_list[i-1],self.vol_list[i-1],self.amount_list[i-1]]
            self.data_train.append(np.array(train))

            if self.close_list[i]/self.close_list[i-1] > 1.0:
                self.data_target.append(float(1.00))
                self.data_target_onehot.append([1,0,0])
            else:
                self.data_target.append(float(0.00))
                self.data_target_onehot.append([0,1,0])
        '''
        real = pd.DataFrame()
        real['1'] = df['close'][1:len(df)].values
        real['0'] = df['close'][0:len(df)-1].values
        real['real'] = real['1']>real['0']
        real.loc[real['real']==True] = 1
        self.data_target = real['real'].values
        '''
        self.cnt_pos =len([x for x in self.data_target if x == 1.00])
        #self.test_case = np.array([self.open_list[-1],self.close_list[-1],self.high_list[-1],self.low_list[-1],self.vol_list[-1],self.amount_list[-1]])
        self.test_case = [[self.open_list[-1],self.close_list[-1],self.high_list[-1],self.low_list[-1],self.vol_list[-1],self.amount_list[-1]]]
        #self.data_train = np.array(self.data_train)
        #self.data_target = np.array(self.data_target)

        '''
        self.test_case = df[['open', 'close', 'high', 'low', 'vol', 'amount']][len(df) - 1:].values
        self.cnt_pos =len([x for x in self.data_target if x == 1.00])
        '''
        return

i=dcds()