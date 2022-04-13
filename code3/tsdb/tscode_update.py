import dbbase

class tscode_update:
    api_name = ''
    data = None
    dbb = None
    pro = None

    def __init__(self):
        self.api_name = 'tscode_update'
        self.dbb = dbbase.dbbase(self.api_name)
        return

   def api_query(self):
        pro = dbb.pro
        df = pro.query(self.api_name,
                       exchange='',
                       list_status='L',
                       fields='ts_code,symbol,name')
        return df

    def load_api(self):
        df = self.api_query()
        dt = date.today()
        np.savez(self.file_path, values=df.values, columns=df.columns, date=dt)
        self.data = np.load(self.file_path, allow_pickle=True)
        return
