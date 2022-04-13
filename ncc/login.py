from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#browser = webdriver.Firefox()
browser = webdriver.Chrome()

browser.get('http://erp.cxic.com:8081/nccloud/resources/uap/rbac/login/main/index.html')
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='login-button submit']")))

# 等待整个网页加载完成，则(By.XPATH, "/html")
assert '大型企业数字化平台' in browser.title
xpath = "//div[@fieldid='group']"
browser.find_element(By.XPATH, xpath).click()
WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, xpath)))
xpath = "//div[@fieldid='group_select']//li[contains(.,'新华昌集团')]"
browser.find_element(By.XPATH, xpath).click()

elem = browser.find_element(By.ID,'username')
elem.send_keys('huangjy')
elem = browser.find_element(By.ID,'password')
elem.send_keys('Yellow@163.com')
#elem = browser.find_element(By.ID,'rand')


#elem = browser.find_element(By.XPATH, "//button[@class='login-button submit']")
#elem = browser.find_element(By.XPATH, "//button[contains(.,'登录')]")
#elem = browser.find_element(By.XPATH, "//div[@id='login_div']/div/div[3]/div[3]/div/div/div[6]/button")


#elem = browser.find_element(By.XPATH,"//button[@class='login-button submit']")
#WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'登录')]")))
#WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-logo1")))
WebDriverWait(browser,100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-logo1")))
#alert = browser.switch_to.alert
#alert.accept()
#print("alert accepted")

#browser.quit()