#1.安装selenium安装Chrome的驱动
#2.引入selenium中的Chrome
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
import requests


#3.创建浏览器
browser =Chrome()

#4.让浏览器打开淘宝
browser.get("http://www.taobao.com")

#5.找到页面中的文本框，输入男装.回车
browser.find_element_by_xpath('//*[@id="q"]').send_keys("男装",Keys.ENTER)

#6.让程序等待，用户手动扫码登录淘宝
while browser.current_url.startswith("https://login.taobao.com"):
    print("等待用户扫码进行下一步操作")
    time.sleep(1)

n=1
while 1:

#7.找到页面中的所有item

    items = browser.find_element_by_class_name("m-itemlist").find_element_by_class_name("item")

    for item in items:
        src_path = item.find_element_by_class_name("pic-box").find_element_by_class_name("img").get_attribute("data-src")
        src_path = "http:"+src_path

        #下载这张图片，保存在文件中
        open("f{n}.jpg", mode="wb").write(requests.get(src_path).content)
        n+=1

    browser.find_element_by_class_name("m-page").find_element_by_class_name("next").click()
    time.sleep(2)
    print("下一页")