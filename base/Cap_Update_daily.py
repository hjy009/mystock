import pymysql
from base import my_stock_pool, my_capital
from datasets import ccdy

def cap_update_daily(state_dt):
    #para_norisk = (1.0 + 0.04/365)
    para_norisk = 1
    #db = pymysql.connect(host='127.0.0.1', user='tf', passwd='xhc123', db='stock', charset='utf8')
    #cursor = db.cursor()
    #sql_pool = "select * from my_stock_pool"
    #cursor.execute(sql_pool)
    #done_set = cursor.fetchall()
    done_set = my_stock_pool.i.data
    #db.commit()
    new_lock_cap = 0.00
    for i in range(len(done_set)):
        stock_code = str(done_set['stock_code'].iloc[i])
        stock_vol = float(done_set['hold_vol'].iloc[i])
        #sql = "select * from stock_info a where a.stock_code = '%s' and a.state_dt <= '%s' order by a.state_dt desc limit 1"%(stock_code,state_dt)
        #cursor.execute(sql)
        #done_temp = cursor.fetchall()
        done_temp = ccdy.i.df_stdate(ts_code=stock_code,from_date=state_dt,to_date=state_dt)
        #db.commit()
        if len(done_temp) > 0:
            cur_close_price = ccdy.i.valuebykey(ts_code=stock_code,st_date=state_dt,key='close')
            new_lock_cap += cur_close_price * stock_vol
        else:
            print('Cap_Update_daily Err!!')
            raise Exception
    #sql_cap = "select * from my_capital order by seq asc"
    #cursor.execute(sql_cap)
    #done_cap = cursor.fetchall()
    #db.commit()
    done_cap = my_capital.i.data
    new_cash_cap = float(done_cap['money_rest'].iloc[-1]) * para_norisk
    new_total_cap = new_cash_cap + new_lock_cap
    #sql_insert = "insert into my_capital(capital,money_lock,money_rest,bz,state_dt)values('%.2f','%.2f','%.2f','%s','%s')"%(new_total_cap,new_lock_cap,new_cash_cap,str('Daily_Update'),state_dt)
    #cursor.execute(sql_insert)
    #db.commit()
    seq = my_capital.i.data['seq'].astype(int).max() + 1
    dic = {}
    dic['capital'] = new_total_cap
    dic['money_lock'] = new_lock_cap
    dic['money_rest'] = new_cash_cap
    dic['bz'] = str('Daily_Update')
    dic['state_dt'] = state_dt
    dic['seq'] = seq
    my_capital.i.append_dict(dic)
    return 1