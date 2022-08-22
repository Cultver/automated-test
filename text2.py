from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://192.168.1.251/bsams/front/login.do")
# driver.find_element(By.ID,"taskId").send_keys('77')
# driver.find_element(By.NAME,"loginName").send_keys('student1')
driver.find_element("id","taskId").send_keys('77')
driver.find_element('name','loginName').send_keys('student1')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('student1')
driver.find_element(By.CSS_SELECTOR,"#vericode").send_keys('shtd')
a = driver.find_element(By.XPATH,'//*[@id="fmedit"]/div[2]/div[6]/input')
ActionChains(driver).click(a).perform()

b = driver.find_element_by_link_text("供应商")
ActionChains(driver).click(b).perform()

driver.find_element_by_id('title').send_keys('北京')

# sleep(5)
# driver.implicitly_wait(30)
driver.find_element_by_id('title').send_keys(Keys.CONTROL,'a')
sleep(3)
driver.find_element_by_id('title').send_keys(Keys.CONTROL,'c')
sleep(3)
c = driver.find_element_by_id('title')
ActionChains(driver).click(c).perform()
driver.find_element_by_id('title').send_keys(Keys.CONTROL,'v')
sleep(3)
driver.find_element_by_id('title').send_keys(Keys.CONTROL,'v')
sleep(3)
driver.close()