import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("http://192.168.1.251/bsams/front/login.do")
driver.find_element("id","taskId").send_keys('77')
driver.find_element('name','loginName').send_keys('student1')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('student1')
driver.find_element_by_css_selector("#vericode").send_keys('shtd')
# driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/input').click()
driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/input').submit()
driver.find_element_by_link_text('个人信息').click()
time.sleep(3)
# ActionChains(driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
driver.execute_script("window.scrollTo(0,100)")
# driver.find_element_by_link_text('供应商').click()
# driver.find_element_by_name('title').send_keys("辽宁异界公司")
# time.sleep(3)
# driver.find_element_by_class_name("search_button").click()
time.sleep(3)
driver.close()