from sklearn import svm
import datetime
import numpy as np
import pandas as pd
from datasets import infomations,trade_cal, daily,ccdy
from base import dfs
from base import ev_mid,ev_resu,ccmid,ccresu


def model_eva(stock,state_dt,para_window,para_dc_window):
    # 建评估时间序列, para_window参数代表回测窗口长度
    date_start = (datetime.datetime.strptime(state_dt, '%Y%m%d') - datetime.timedelta(days=para_window)).strftime(
        '%Y%m%d')
    date_end = state_dt
    # 开始回测，其中para_dc_window参数代表建模时数据预处理所需的时间窗长度
    #ccmid.i.set_pds(stock,date_start,date_end,para_dc_window)
    #ccmid.i.set_reals(stock,date_start,date_end)
    # 计算查全率
    ccresu.i.set_f1(stock,date_start,date_end,para_dc_window)
    return 1


if __name__ == '__main__':

    model_eva('002049.SZ','20160311',90,365)

    dfs.i.save_file()
    infomations.i.save_file()
    print('All Finished !!')
