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
    hmenu = None
    hwin = None

    #用__new__实现单例模式
    def __new__(cls, *args, **kwargs):
        if not '_instance' in vars(cls):
            #print 'creating instance of Singleton1'
            cls._instance = super(base, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.login()
        return

    def __del__(self):
#        self.browser.quit()
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

    def login(self):
        self.driver.get('http://erp.cxic.com:8081/nccloud/resources/uap/rbac/login/main/index.html')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='login-button submit']")))
        # 等待整个网页加载完成，则(By.XPATH, "/html")
        assert '大型企业数字化平台' in self.driver.title
        #page_source = browser.page_source
        xp = "//div[@fieldid='group']"
        self.click(xp)
        xp = "//div[@fieldid='group_select']//li[contains(.,'新华昌集团')]"
        self.wait(xp)
        self.click(xp)

        xp = "//input[@fieldid='username']"
        self.wait(xp)
        self.idsendkey('username','huangjy')
        self.idsendkey('password','Yellow@163.com')
#       self.driver.find_element(By.ID, 'rand').click()
        xp = "//button[@fieldid='login_btn']"
        self.click(xp)
        xp = "//button[@fieldid='alert-ok_btn']"
        self.wait(xp)
        if self.isExist(xp):
            self.click(xp)

        #等待输入        #加载首页
        self.waitclick("//i[contains(@class,'icon-logo1')]")
        #assert '首页' in self.driver.title
        self.wait("//div[contains(text(),'动态建模平台')]")
        self.hmenu = self.driver.current_window_handle
        return

    def menu(self,m1,m2):
        #点击主菜单 并进入 iframe
        #点击左边
        self.driver.switch_to.window(self.hmenu)
        ss = "//span[contains(text(),'%s')]"%(m1)
        self.click(ss)
        #点击右边
        ss = "//div[contains(text(),'%s')]"%(m2)
        self.waitclick(ss)
        self.hwin = self.driver.window_handles[-1]
        while (self.hmenu == self.hwin):
            self.hwin = self.driver.window_handles[-1]
        self.iframe()
        return

    def iframe(self):
        #进入iframe
        self.driver.switch_to.window(self.hwin)
        self.driver.switch_to.default_content()
        ss = "//iframe"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        ss = self.driver.find_element(By.XPATH, "//iframe").get_attribute('id')
        self.driver.switch_to.frame('mainiframe')
        return

    def mtree(self, t1, t2):
        #进入tree
        ss = "//span[@class='title-single']/span[contains(.,'%t1')]/.."%(t1)
        self.click(ss)
        ss = "//span[@class='title-single']/span[contains(.,'%t2')]"%(t2)
        self.waitclick(ss)
        self.driver.switch_to.default_content()
        return

    def minput(self, label, value):
        #主表直接输入
        ss = "//div[(@class='form-item-label') and (@title='%s')]/..//input"%(label)
        self.wait(ss)
        #WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        #elem = self.browser.find_element(By.XPATH,"//div[(@class='form-item-label') and (@title='"+label+"')]/..//div[@class='u-col-xs-12 refer clearfix   refer-input-disabled']")
        ss = "//div[(@class='form-item-label') and (@title='%s')]/..//div[contains(@class,'template-item-wrapper')]"%(label)
        self.waitclick(ss)
        ss = "//div[(@class='form-item-label') and (@title='%s')]/..//div[contains(@class,'refer-wrapper')]" % (label)
        self.click(ss)

        ss = "//div[(@class='form-item-label') and (@title='%s')]/..//div[contains(@class,'u-col-xs-12')]"%(label)
        self.click(ss)
        ss = "//div[(@class='form-item-label') and (@title='%s')]/..//div/input"%(label)
        self.sendkey(ss,value)
        ss = "//div[contains(@class,'u-dropdown')]//li[contains(.,'%s')]"%(value)
        self.wait(ss)
        return

    def minputpop(self, label, value):
        #主表弹出选择
        ss = "//div[(@class='form-item-label') and (@title='"+label+"')]/..//input"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        #elem = self.browser.find_element(By.XPATH,"//div[(@class='form-item-label') and (@title='"+label+"')]/..//div[@class='u-col-xs-12 refer clearfix   refer-input-disabled']")
        elem = self.driver.find_element(By.XPATH, "//div[(@class='form-item-label') and (@title='" + label + "')]/..//div[contains(@class,'template-item-wrapper')]")
        elem.click()
        elem = self.driver.find_element(By.XPATH, "//div[(@class='form-item-label') and (@title='" + label + "')]/..//div[contains(@class,'refer-wrapper')]")
        elem.click()
        elem = self.driver.find_element(By.XPATH, "//div[(@class='form-item-label') and (@title='" + label + "')]/..//div[contains(@class,'u-col-xs-12')]")
        elem.click()

        elem = self.driver.find_element(By.XPATH, "//div[(@class='form-item-label') and (@title='" + label + "')]/..//span[@class='icon-refer']")
        elem.click()
        ss = "//div[@class='loading-container']//div[ @title='"+value+"']"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        elem = self.driver.find_element(By.XPATH, "//div[@class='loading-container']//div[ @title='" + value + "']")
        elem.click()
        #//div[@class='loading-container']//div[@class='u-table-scroll']//tr[2]
        ss = "//div[@class='loading-container']//tr[ contains(@class,'refer-selected-row')]//div[@title='"+value+"']"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        elem = self.driver.find_element(By.XPATH, "//div[@class='loading-container']//button[contains(.,'确定')]")
        elem.click()
        #

        #清空确认
        ss = "//div[(@class='form-item-label') and (@title='"+label+"')]/..//div/input[ @value='"+value+"']"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        elems = self.driver.find_elements(By.XPATH, "//div[@class='u-modal-dialog u-modal-draggable']//button[contains(.,'确定')]")
        if len(elems) >0:
            elems[0].click()

        return

    def minputpopi(self, label, idx):
        #主表弹出选择序号
        ss = "//div[(@class='form-item-label') and (@title='"+label+"')]/..//input"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        #elem = self.browser.find_element(By.XPATH,"//div[(@class='form-item-label') and (@title='采购组织')]/..//div[@class='u-col-xs-12 refer clearfix   refer-input-disabled']")
        elem = self.driver.find_element(By.XPATH, "//div[(@class='form-item-label') and (@title='" + label + "')]/..//div[contains(@class,'template-item-wrapper')]")
        elem.click()
        elem = self.driver.find_element(By.XPATH, "//div[(@class='form-item-label') and (@title='" + label + "')]/..//div[contains(@class,'refer-wrapper')]")
        elem.click()
        elem = self.driver.find_element(By.XPATH, "//div[(@class='form-item-label') and (@title='" + label + "')]/..//div[contains(@class,'u-col-xs-12')]")
        elem.click()

        elem = self.driver.find_element(By.XPATH, "//div[(@class='form-item-label') and (@title='" + label + "')]/..//span[@class='icon-refer']")
        elem.click()
        ss = "//div[@class='loading-container']//div[@class='u-table-scroll']//tr["+str(idx)+"]"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
#        elem = self.browser.find_element(By.XPATH, "//div[@class='loading-container']//tr["+str(idx)+"]")
        elem = self.driver.find_element(By.XPATH, "//div[@class='loading-container']//tr[@data-row-index=" + str(idx) + "]")
        elem.click()
        value = elem.get_attribute('title')
        #//div[@class='loading-container']//div[@class='u-table-scroll']//tr[2]
        ss = "//div[@class='loading-container']//tr[contains(@class,'refer-selected-row') and @data-row-index="+str(idx)+"]"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        elem = self.driver.find_element(By.XPATH, "//div[@class='loading-container']//button[contains(.,'确定')]")
        elem.click()
        #
        #清空确认
        ss = "//div[(@class='form-item-label') and (@title='"+label+"')]/..//div/input[ @value='"+value+"']"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        elems = self.driver.find_elements(By.XPATH, "//div[@class='u-modal-dialog u-modal-draggable']//button[contains(.,'确定')]")
        if len(elems) >0:
            elems[0].click()

        return

    def minputdt(self, label, value):
        #主表输入日期
        ss = "//div[(@class='form-item-label') and (@title='"+label+"')]/..//input"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        elem = self.driver.find_element(By.XPATH, "//div[(@class='form-item-label') and (@title='" + label + "')]/..//div[contains(@class,'template-item-wrapper')]")
        elem.click()

        elem = self.driver.find_element(By.XPATH, "//input[@class='rc-calendar-input ']")
        elem.send_keys(value)
        return

    def dinput(self,col,label,value):
        #明细表输入

        ss = "//thead//span[contains(.,'"+label+"')]/.."
        elem = self.driver.find_element(By.XPATH, ss)
        idx = int(elem.get_attribute('data-col-index'))+1
        ss = "//tbody//tr["+str(col)+"]//td["+str(idx)+"]//span[contains(@class,'template-item-wrapper')]"
        elem = self.driver.find_element(By.XPATH, ss)
        elem.click()
        #time.sleep(5)
        ss = "//tbody//tr["+str(col)+"]//td["+str(idx)+"]//div/input"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        elem = self.driver.find_element(By.XPATH, ss)
        elem.send_keys(value)
        return

    def dinputpop(self,col, label, value):
        # 明细表输入

        ss = "//thead//span[contains(.,'" + label + "')]/.."
        elem = self.driver.find_element(By.XPATH, ss)
        idx = int(elem.get_attribute('data-col-index')) + 1
        ss = "//tbody//tr["+str(col)+"]//td[" + str(idx) + "]//span[contains(@class,'template-item-wrapper')]"
        elem = self.driver.find_element(By.XPATH, ss)
        elem.click()
        ss = "//tbody//tr["+str(col)+"]//td["+str(idx)+"]//div/input"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        ss = "//tbody//tr["+str(col)+"]//td["+str(idx)+"]//span[contains(@class,'icon-refer')]"
        elem = self.driver.find_element(By.XPATH, ss)
        elem.click()

        # div title='0501010001'
        #//div[@class='refer-tree ']//span[@class='refer-tree-title' and contains(.,'050101')]
        #//div[@class='refer-td' and @title='0501010001']
        #//div[contains(@class,'refer-pop-window-show')]//button[contains(.,'确定')]
        sst = value[:2]
        ss = "//div[@class='refer-tree ']//span[@class='refer-tree-title' and contains(.,'"+sst+"')]"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        elem = self.driver.find_element(By.XPATH, ss)
        elem.click()
        sst = value[:4]
        ss = "//div[@class='refer-tree ']//span[@class='refer-tree-title' and contains(.,'"+sst+"')]"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        elem = self.driver.find_element(By.XPATH, ss)
        elem.click()
        sst = value[:6]
        ss = "//div[@class='refer-tree ']//span[@class='refer-tree-title' and contains(.,'"+sst+"')]"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        elem = self.driver.find_element(By.XPATH, ss)
        elem.click()
        ss = "//div[@class='refer-td' and @title='"+value+"']"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, ss)))
        elem = self.driver.find_element(By.XPATH, ss)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(elem).perform()


        #//button[contains(.,'保存')]
        #//button[contains(.,'暂存')]
        #//button[contains(.,'保存提交')]
        #//div[@class='nc-bill-top-area']//button[contains(.,'取消')]
        return
