from base import filedf


class my_stock_pool(filedf.filedf):

    def __init__(self, api_name='my_stock_pool'):
        super(my_stock_pool, self).__init__(api_name)
        self.load_file()
        return

    def default_columns(self):
        if len(self.data)==0:
            dCols = ['stock_code', 'buy_price', 'hold_vol', 'hold_days']
        else:
            dCols = self.data.columns
        return dCols

i = my_stock_pool()