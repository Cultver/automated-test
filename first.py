import time
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://192.168.1.251/ceshi/front/login.do")
# print(driver.title)#打印页面标题
# sleep(2)#时间等待方法1
driver.maximize_window()#最大化windows窗口
#
# driver.get("https://www.bing.com/")
# print(driver.title)
# driver.back()


# driver.refresh()#刷新
# time.sleep(2)#时间等待方法2
# driver.forward()
#driver.quit()#退出窗口
#time.sleep(2)
#driver.close()#关闭当前页面
#time.sleep(1)







