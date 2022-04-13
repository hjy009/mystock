from base import filedf


class my_capital(filedf.filedf):

    def __init__(self, api_name='my_capital'):
        super(my_capital, self).__init__(api_name)
        #INSERT INTO `my_capital` VALUES(1000000.00, 0.00, 1000000.00, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL);
        self.load_file()
        if len(self.data) ==0 :
            dic = dict(zip(self.default_columns(), [1000000.00, 0.00, 1000000.00, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]))
            self.append_dict(dic)
        return

    def default_columns(self):
        if len(self.data)==0:
            dCols = ['capital', 'money_lock', 'money_rest', 'deal_action',
                          'stock_code', 'deal_price', 'stock_vol', 'profit',
                          'profit_rate', 'bz', 'state_dt', 'seq',
                          'score']
        else:
            dCols = self.data.columns
        return dCols

i = my_capital()