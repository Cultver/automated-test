import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("http://192.168.1.251/bsams/front/login.do")
driver.find_element("id","taskId").send_keys('77')
driver.find_element('name','loginName').send_keys('student3')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('student3')
driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/input').click()
a = driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/a')
ActionChains(driver).click(a).perform()
driver.switch_to_window(driver.window_handles[1])
time.sleep(3)
driver.close()