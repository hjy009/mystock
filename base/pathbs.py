import os


class pathbs:
    root = ''
    path1 = ''
    modified = False

    #用__new__实现单例模式
    def __new__(cls, *args, **kwargs):
        if not '_instance' in vars(cls):
            #print 'creating instance of Singleton1'
            cls._instance = super(pathbs, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self,root='.mystock',child='base'):
        self.root = os.path.join(os.path.expanduser('~'), root)
        self.path1 = os.path.join(self.root, child)
        return

    def __del__(self):
        if self.modified :
            #self.save_file()
            print('%s 调用__del__() 没有保存对象' % (type(self).__name__))
        #print("pathbs调用__del__() 销毁对象，释放其空间")
        #super(infomations, self).__del__(self)

    def path1f(self,fname, hz='.csv'):
        path = os.path.join(self.path1, fname + hz)
        return path


    def pathapi(self,api):
        path = self.path1f(api)
        return path


    def path2(self,child):
        path = os.path.join(self.path1, child)
        return path


    def path2f(self,child, fname):
        path = os.path.join(self.path2(child), fname + '.csv')
        return path

    def pathapi2(self,child,fname):
        path = self.path2f(child, fname)
        return path

    def path3(self,childs):
        path = self.path1
        for i in range(len(childs)):
            path = os.path.join(path, childs[i])
        return path

    def path3f(self,childs, fname):
        path = self.path3(childs)
        path = os.path.join(path, fname + '.csv')
        return path

    def pathapi3(self,childs,fname):
        path = self.path3f(childs,fname)
        return path

    def get_infopath(self):
        path = self.pathapi('infomation')
        return path

    def get_dailypath(self,s_code):
        path = self.pathapi2('daily',ts_code)
        return path

    def get_barpath(self,ts_code,adj='qfq'):
        path = self.pathapi3(['bar',adj],ts_code)
        return path

pth = pathbs()