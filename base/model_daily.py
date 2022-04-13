from base import filedf,pathbs
import pandas as pd
import datetime

class model_daily(filedf.filedf):
    stock_code = '0000001.SZ'
    ftime_name = 'trade_date'

    def __init__(self, api_name='daily',stock_code='0000001.SZ'):
        self.stock_code = stock_code
        super(model_daily, self).__init__(api_name)
        self.load_file()
        return

    def get_filepath(self):
        res = pathbs.pth.pathapi2(self.api_name,self.stock_code)
        return res

    def default_columns(self):
        if len(self.data)==0:
            dCols = ['trade_date','stock_code']
        else:
            dCols = self.data.columns
        return dCols

    def api_query(self):
        df = pd.DataFrame(data=[], columns=self.dCols)
        return df

    def append_data(self, df):
        self.data = df.combine_first(self.data)
        return

    def append_dict(self,dic):
        df = pd.DataFrame(data=dic,index=[dic[self.ftime_name]])
        df.index = df[self.ftime_name].astype(str).astype('datetime64')
        self.data = df.combine_first(self.data)
        return

