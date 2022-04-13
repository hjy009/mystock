'''

'''
import tushare as ts
# import numpy as np
import pandas as pd
import os
import time
from base import dfinfo,pathbs


class filedf(dfinfo.dfinfo):
    data = pd.DataFrame()

    def __init__(self, api_name):
        super(filedf, self).__init__(api_name)
        return

    def get_filepath(self):
        res = pathbs.pth.pathapi(self.api_name)
        return res

    def default_columns(self):
        if len(self.data)==0:
            dCols = ['infomation', 'start_date', 'end_date', 'list_date', 'file_date']
        else:
            dCols = self.data.columns
        return dCols

    def init(self):
        self.load_data()
        return

    def save(self):
        self.save_file()
        self.save_info()
        return

    def expire(self):
        resu = False
        if time.strftime("%Y%m%d", self.eddate) <= time.strftime("%Y%m%d", time.localtime()):
            if time.struct_time(self.eddate).tm_hour < 19:
                resu = True
        return resu

    def load_data(self):
        if self.load_file():
            if self.expire():
                self.load_api()
        else:
            self.load_api()
        return

    def before_query(self):
        self.eddate = time.localtime()
        return

    def api_query(self):
        df = pd.DataFrame(data=[], columns=self.default_columns())
        return df

    def after_query(self, df):
        self.reflesh_data(df)
        self.save_file()
        self.stdate = self.eddate
        self.save_info()
        return

    def append_data(self, df):
        self.data = self.data.append(other=df, ignore_index=True)
        return

    def reflesh_data(self, df):
        self.append_data(df)
        # np.savez(self.file_path,values=df.values,columns=df.columns,infomation=self.info)
        # self.data = np.load(self.file_path, allow_pickle=True)
        return

    def load_api(self):
        self.before_query()
        df = self.api_query()
        self.after_query(df)
        return

    def befault_loadf(self):
        return

    def load_file(self):
        succ = False
        if os.path.exists(self.get_filepath()):
            self.befault_loadf()
            self.data = pd.read_csv(filepath_or_buffer=self.get_filepath(), index_col=0)
            # self.data = np.load(self.file_path, allow_pickle=True)
            self.after_loadf()
            succ = True
        else:
            self.data = pd.DataFrame(data=[], columns=self.default_columns())
        return succ

    def after_loadf(self):
        if len(self.data)>0:
            self.dCols = self.data.columns
        self.load_info()
        # self.info = pd.read_csv(filepath_or_buffer=paths.get_infopath())
        # self.eddate = time.strptime(self.info[0],"%Y-%m-%d")
        return

    def save_file(self):
        self.data.to_csv(path_or_buf=self.get_filepath(), index_label='key')
        return

    def append_array(self,ary):
        dic = dict(zip(self.dCols, ary))
        self.append_dict(dic)
        return

    def append_dict(self,dic):
        self.data = self.data.append(other=dic, ignore_index=True)
        return

    def dropkeyvalue(self,key,value):
        self.data.drop(index=self.data.loc[self.data[key].astype(str) == str(value)].index,inplace=True)
        return