import pymysql.cursors
from base import  my_capital,my_stock_pool
from datasets import  ccdy
from datasets import daily

class Deal(object):
    cur_capital = 0.00
    cur_money_lock = 0.00
    cur_money_rest = 0.00
    stock_pool = []
    mprice = {}
    mvol = {}
    mdays = {}
    stock_all = []
    ban_list = []

    def __init__(self,state_dt):
        # 建立数据库连接
        #db = pymysql.connect(host='127.0.0.1', user='tf', passwd='xhc123', db='stock', charset='utf8')
        #cursor = db.cursor()
        #sql_select = 'select * from my_capital a order by seq desc limit 1'
        #cursor.execute(sql_select)
        #done_set = cursor.fetchall()
        df = my_capital.i.data.sort_values(by='seq',ascending=False)
        self.cur_capital = 0.00
        self.cur_money_lock = 0.00
        self.cur_money_rest = 0.00
        '''
        if len(done_set) > 0:
            self.cur_capital = float(done_set[0][0])
            self.cur_money_rest = float(done_set[0][2])
        '''
        if len(df) >0:
            self.cur_capital = df['capital'].iloc[0]
            self.cur_money_rest = df['money_rest'].iloc[0]
        #sql_select2 = 'select * from my_stock_pool'
        #cursor.execute(sql_select2)
        #done_set2 = cursor.fetchall()

        self.stock_pool = []
        self.stock_all = []
        self.mprice = []
        self.mvol = []
        self.mdays = []
        self.ban_list = []
        done_set2 = my_stock_pool.i.data
        if len(done_set2) > 0:
            self.stock_pool = done_set2.loc[(done_set2['hold_vol']>0)]['stock_code'].values
            self.stock_all = done_set2['stock_code'].values
            self.mprice = dict(zip(done_set2['stock_code'],done_set2['buy_price']))
            self.mvol = dict(zip(done_set2['stock_code'],done_set2['hold_vol']))
            self.mdays = dict(zip(done_set2['stock_code'],done_set2['hold_days']))
        for i in range(len(done_set2)):
            #sql = "select * from stock_info a where a.stock_code = '%s' and a.state_dt = '%s'" % (
            #done_set2[i][0], state_dt)
            #cursor.execute(sql)
            #done_temp = cursor.fetchall()
            #db.commit()
            str = done_set2['stock_code'].iloc[i]
            self.cur_money_lock += ccdy.i.valuebykey(ts_code=str,st_date=state_dt,key='close') * done_set2['hold_vol'].iloc[i]
            #dy.load_info()
            #done_temp = dy.data.loc[(dy.data['stock_code']==done_set2[i][0])&(dy.data['state_dt']==state_dt)]
            #self.cur_money_lock += float(done_temp[0][3]) * float(done_set2[i][2])
        # sql_select3 = 'select * from ban_list'
        # cursor.execute(sql_select3)
        # done_set3 = cursor.fetchall()
        # if len(done_set3) > 0:
        #     self.ban_list = [x[0] for x in done_set3]


