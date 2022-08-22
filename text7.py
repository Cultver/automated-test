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
driver.find_element_by_link_text('个人信息').click()
driver.find_element_by_link_text('保存').click()
time.sleep(5)
driver.(switch_to_alert).accept()
time.sleep(5)
driver.close()