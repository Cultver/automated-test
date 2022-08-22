from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("http://192.168.1.251/bsams/front/login.do")
time.sleep(30)
driver.maximize_window()
driver.find_element_by_id('taskId').send_keys("77")
driver.find_element_by_name('loginName').send_keys("student3")
driver.find_element_by_id('password').send_keys("student3")
driver.find_element_by_id("vericode").send_keys("shtd")
driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/input').submit()
driver.find_element_by_link_text('存放地点').click()
a = driver.find_element_by_name("status")
Select(a).select_by_visible_text('已禁用')
time.sleep(30)
driver.close()
