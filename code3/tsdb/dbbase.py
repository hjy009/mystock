import pymysql
import tushare as ts

class dbbase:
    table_name = ''
    db = pymysql.connect(host='127.0.0.1', user='tf', passwd='xhc123', db='stock', charset='utf8')
    pro = ts.pro_api()

    def __init__(self, table_name='tscode_update'):
        self.table_name = api_name
        return

