from base import model_daily


class ev_resu(model_daily.model_daily):

    def __init__(self, api_name='ev_resu',stock_code='0000001.SZ'):
        super(ev_resu, self).__init__(api_name=api_name,stock_code=stock_code)
        return

    def default_columns(self):
        if len(self.data)==0:
            dCols = ['trade_date','stock_code','acc','recall','f1','acc_neg','bz','predict']
        else:
            dCols = self.data.columns
        return dCols

