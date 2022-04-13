from base import model_daily


class ev_mid(model_daily.model_daily):

    def __init__(self, api_name='ev_mid',stock_code='0000001.SZ'):
        super(ev_mid, self).__init__(api_name=api_name,stock_code=stock_code)
        return

    def default_columns(self):
        if len(self.data)==0:
            dCols = ['trade_date','stock_code','resu_predict','resu_real']
        else:
            dCols = self.data.columns
        return dCols

