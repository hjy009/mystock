from sklearn import svm
from base import dcds, ev_mid,ccmid,dfs,ccresu
from datasets import ccdy,trade_cal
import datetime
import numpy as np

def set_svm1():
    stock = '002049.SZ'
    #dc1 = DC.data_collect(stock, '2017-03-01', '2018-03-01')
    dc = dcds.i
    dc.collectDATA(stock,'20170301','20180301')
    model = svm.SVC()               # 建模
    model.fit(dc.data_train, dc.data_target)        # 训练
    ans2 = model.predict(dc.test_case) # 预测
    # 输出对2018-03-02的涨跌预测，1表示涨，0表示不涨。
    print(ans2[0])
    dic = {}
    dic['state_dt'] = '20180301'
    dic['stock_code'] = stock
    sl = str(365)
    dic[sl] = ans2[0]
    em = ev_mid.ev_mid()
    em.append_dict(dic)
    em.save()
    return

def set_predict(stock,para_window):
    df = ccdy.i.df_stock(ts_code=stock)
    mid = ccmid.i.df_stock(stock)
    if len(mid) > 0:
        from_date = mid['trade_date'].iloc[-1].astype(int).astype(str)
    else:
        dt = df['trade_date'].iloc[0].astype(int).astype(str)
        from_date = (datetime.datetime.strptime(dt, '%Y%m%d') + datetime.timedelta(days=para_window)).strftime(
            '%Y%m%d')
    to_date = df['trade_date'].iloc[-1].astype(int).astype(str)
    df = ccdy.i.df_stdate(stock,from_date,to_date)

    date_seq = df['trade_date'].astype(int).astype(str)


    # 数据准备
    for dt in date_seq:
        ccmid.i.set_predict(stock,dt,para_window)
    return

def set_reals(stocks):
    for stock in stocks:
        mid = ccmid.i.df_stock(stock)
        mid = mid.loc[mid['resu_real'].isna()]
        if len(mid) > 1:
            from_date = mid['trade_date'].iloc[0].astype(int).astype(str)
            to_date = mid['trade_date'].iloc[-1].astype(int).astype(str)
            ccmid.i.set_reals(stock,from_date,to_date)
    return

def set_ps(stocks,para_window):
    for stock in stocks:
        set_predict(stock, para_window)
    return

def set_fs(stocks,f1_window,pre_window):
    for stock in stocks:
        df = ccmid.i.df_stock(stock)
        dt = df['trade_date'].iloc[0].astype(int).astype(str)
        from_date = (datetime.datetime.strptime(dt, '%Y%m%d') + datetime.timedelta(days=f1_window)).strftime(
            '%Y%m%d')
        to_date = df['trade_date'].iloc[-1].astype(int).astype(str)
        df = ccresu.i.df_stock(stock)
        df = df.loc[df['resu_real'].isna()]
        if len(df)>0:
            dt = df['trade_date'].iloc[0].astype(int).astype(str)
            if dt > from_date:
                from_date = dt
        ccresu.i.set_fs(stock,from_date,to_date,f1_window,pre_window)

    return

if __name__ == '__main__':
    #set_svm1()

    #stock_pool = ['603912.SH', '300666.SZ', '300618.SZ', '002049.SZ', '300672.SZ']
    stock_pool = ['002049.SZ']
    pre_window = 365
    f1_window = 90
    #set_ps(stock_pool,pre_window)
    #set_reals(stock_pool)
    #set_fs(stock_pool,f1_window,pre_window)

    dfs.i.save_file()
    print('All Finished !!')

