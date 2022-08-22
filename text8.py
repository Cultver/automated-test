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
driver.find_element_by_link_text('资产类别').click()
driver.find_element_by_css_selector('body > div.border_bg > div > div.main_con.right > div.current_bottom > div.search_border > div > input').click()
# driver.find_element_by_name('title').send_keys('45s')
# driver.find_element_by_id('code').send_keys('12a')
# driver.find_element_by_link_text('保存').click()
# driver.switch_to_alert().accept()
# driver.switch_to_alert().dismiss()
driver.switch_to_alert().send_keys('45a')
a = driver.switch_to_alert().text
print(a)
time.sleep(3)
driver.close()