import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://192.168.1.251/ceshi/front/login.do")
driver.find_element_by_id("loginName").send_keys("student1")
driver.find_element_by_css_selector('#pwd').send_keys("student1")
# driver.find_element_by_id("pwd").send_keys("student1")
# driver.find_element_by_name("loginname").send_keys("student")
# driver.find_element_by_name("password").send_keys("student1")
driver.find_element_by_xpath('//*[@id="fmedit"]/div/div[5]/input').click()
driver.find_element_by_link_text('测试训练1').click()
# time.sleep(2)
# driver.find_element_by_link_text('http://192.168.1.251/bsams/front/login.do').click()
driver.get("http://192.168.1.251/bsams/front/login.do")
# driver.find_element_by_name("taskId").send_keys("77")
# driver.find_element_by_id("loginName").send_keys("student1")
# driver.find_element_by_css_selector("#password").send_keys("student1")
# driver.find_element_by_name("vericode").send_keys("shtd")
driver.find_elements_by_tag_name("input")[0].send_keys("77")
driver.find_elements_by_tag_name("input")[1].send_keys("student1")
driver.find_elements_by_tag_name("input")[2].send_keys("student1")
driver.find_elements_by_tag_name("input")[3].send_keys("shtd")
driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/input').click()
# driver.find_element_by_link_text('个人信息').click()
# driver.find_element_by_class_name('nickname').send_keys("15052639281")
driver.find_element_by_link_text('供应商').click()
driver.find_element_by_name('title').send_keys("北京")
driver.find_element_by_class_name("search_button").click()
time.sleep(5)
# driver.close()
