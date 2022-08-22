import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("http://192.168.1.251/bsams/front/login.do")
driver.find_element("id","taskId").send_keys('77')
driver.find_element('name','loginName').send_keys('student1')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('student1')
# driver.find_element_by_css_selector("#vericode").send_keys('shtd')
# driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/input').click()
driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/input').submit()
a = driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/a')
driver.execute_script("arguments[0].removeAttribute('target')",a)
a.click()
time.sleep(3)
driver.close()