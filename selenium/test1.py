from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Firefox()
browser = webdriver.Chrome()

browser.get('http://www.baidu.com')
assert '百度' in browser.title

elem = browser.find_element(By.ID, 'kw')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

#browser.quit()