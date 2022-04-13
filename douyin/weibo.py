from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from douyin import base

class weibo(base.base):
    dCols = ['key', 'url']
    def baseurl(self):
        self.driver.get('https://s.weibo.com/top/summary?cate=realtimehot')
        self.wait("//tr[52]/td[2]")
        return

    def get_filepath(self):
        str = 'weibo.csv'
        return str

    def top(self):
        self.data = pd.DataFrame(data=[], columns=self.dCols)
        self.data.to_csv(path_or_buf=self.get_filepath(), index_label='id')
        # 等待整个网页加载完成，则(By.XPATH, "/html")
        for i in range(2,52):
            xp = "//tr[%d]/td[2]"% (i)
            elem = self.driver.find_element(By.XPATH, xp)
            key = elem.text
            xp = "//tr[%d]/td[2]/a" % (i)
            elem = self.driver.find_element(By.XPATH, xp)
            url = elem.get_attribute('href')
            df = pd.DataFrame(data=[[key,url]], columns=self.dCols,index=[i-1])
            self.data = self.data.append(df)
            #str = elem.text
            #str = elem.get_attribute("href")

        self.save_file()


        return
