import pymysql
import Model_Evaluate as ev
import Filter
import Portfolio as pf
from pylab import *
import Cap_Update_daily as cap_update
import tushare as ts
from base import my_capital,my_stock_pool,ccresu
from datasets import trade_cal

def get_sharp_rate():
    done_exp = my_capital.i.data
    cap_list = done_exp['capital'].values
    return_list = []
    base_cap = done_exp['capital'].iloc[0]
    for i in range(len(cap_list)):
        if i == 0:
            return_list.append(float(1.00))
        else:
            ri = (float(done_exp['capital'].iloc[i]) - float(done_exp['capital'].iloc[0]))/float(done_exp['capital'].iloc[0])
            return_list.append(ri)
    std = float(np.array(return_list).std())
    exp_portfolio = (float(done_exp['capital'].iloc[-1]) - float(done_exp['capital'].iloc[0]))/float(done_exp['capital'].iloc[0])
    exp_norisk = 0.04*(5.0/12.0)
    sharp_rate = (exp_portfolio - exp_norisk)/(std)

    return sharp_rate,std

if __name__ == '__main__':

    year = 2020
    date_seq_start = str(year) + '0101'
    date_seq_end = str(year) + '1201'
    stock_pool = ['603912.SH', '300666.SZ', '300618.SZ', '002049.SZ', '300672.SZ']

    # 先清空之前的测试记录,并创建中间表
    if len(my_capital.i.data) >1:
        my_capital.i.data.drop(index=my_capital.i.data.loc[(my_capital.i.data['seq'].astype(int) !=1)].index,inplace=True)
    my_stock_pool.i.data.drop(index=my_stock_pool.i.data.index,inplace=True)

    # 建回测时间序列
    back_test_date_start = (datetime.datetime.strptime(date_seq_start, '%Y%m%d')).strftime('%Y%m%d')
    back_test_date_end = (datetime.datetime.strptime(date_seq_end, "%Y%m%d")).strftime('%Y%m%d')
    df = trade_cal.date_range(from_date=date_seq_start,to_date=date_seq_end,is_open=1)
    date_seq = df.astype(str)

    #数据准备 SVM

    #开始模拟交易
    index = 1
    day_index = 0
    for i in range(1,len(date_seq)):
        day_index += 1
        # 每5个交易日更新一次配仓比例
        if divmod(day_index+4,5)[1] == 0:
            portfolio_pool = stock_pool
            if len(portfolio_pool) < 5:
                print('Less than 5 stocks for portfolio!! state_dt : ' + str(date_seq[i]))
                continue
            pf_src = pf.get_portfolio(portfolio_pool,date_seq[i-1],90)
            # 取最佳收益方向的资产组合
            risk = pf_src[1][0]
            weight = pf_src[1][1]
            Filter.filter_main(portfolio_pool,date_seq[i],date_seq[i-1],weight)
        else:
            Filter.filter_main([],date_seq[i],date_seq[i - 1], [])
            cap_update_ans = cap_update.cap_update_daily(date_seq[i])
        print('Runnig to Date :  ' + str(date_seq[i]))
    my_stock_pool.i.save()
    my_capital.i.save()
    print('ALL FINISHED!!')


    sharp,c_std = get_sharp_rate()
    print('Sharp Rate : ' + str(sharp))
    print('Risk Factor : ' + str(c_std))



