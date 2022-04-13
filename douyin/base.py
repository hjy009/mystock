from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import numpy as np
import os,time
#from datasets import paths

class base:
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    data = None

    #用__new__实现单例模式
    def __new__(cls, *args, **kwargs):
        if not '_instance' in vars(cls):
            #print 'creating instance of Singleton1'
            cls._instance = super(base, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.data = pd.DataFrame()
        self.baseurl()
        return

    def __del__(self):
        self.driver.close()
        return

    def baseurl(self):

        return

    def get_filepath(self):
        str = 'base.csv'
        return str

    def save_file(self):
        self.data.to_csv(path_or_buf=self.get_filepath(),index_label='key')
        return

    def idsendkey(self,id,value):
        elem = self.driver.find_element(By.ID, id)
        elem.send_keys(value)
        return

    def sendkey(self,xpath,value):
        elem = self.driver.find_element(By.XPATH, xpath)
        elem.send_keys(value)
        return

    def isExist(self,xpath):
        elems = self.driver.find_elements(By.XPATH, xpath)
        if len(elems) > 0:
            res = True
        else:
            res = False
        return res

    def click(self,xpath):
        self.driver.find_element(By.XPATH, xpath).click()
        return

    def wait(self,xpath):
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return

    def waitclick(self,xpath):
        self.wait(xpath)
        self.click(xpath)
        return


