import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("http://192.168.1.251/bsams/front/login.do")
driver.find_element("id","taskId").send_keys('77')
driver.find_element('name','loginName').send_keys('student1')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('student1')
driver.find_element_by_css_selector("#vericode").send_keys('shtd')
driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/input').submit()
driver.find_element_by_link_text('资产借还').click()
# driver.find_elements_by_tag_name("option")[2].click()
# driver.find_element_by_xpath('//*[@id="assetCategoryId"]/option[2]').click()
a = driver.find_element_by_name('assetCategoryId')
# Select(a).select_by_visible_text("87")
# Select(a).select_by_value("387")
Select(a).select_by_index("1")
# driver.find_element_by_name('file').send_keys(r'D:\Pycharm\untitled2.png')#本地文件添加
# driver.find_element_by_name('file').send_keys('D:\\Pycharm\\untitled2.png')
# driver.find_element_by_name('file').send_keys('D:/Pycharm/untitled2.png')
driver.get_screenshot_as_file(r'D:\EDGE\chromedriver.png')#截屏
time.sleep(3)
driver.close()