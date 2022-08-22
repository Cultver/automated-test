import unittest
import time
from selenium import webdriver
class Denglu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.quit()
    def test_denglu01(self):
        self.driver.get("http://192.168.1.251/bsams/front/login.do")
        self.driver.find_elements_by_tag_name("input")[0].send_keys("77")
        self.driver.find_elements_by_tag_name("input")[1].send_keys("student1")
        self.driver.find_elements_by_tag_name("input")[2].send_keys("student1")
        self.driver.find_elements_by_tag_name("input")[3].send_keys("shtd")
        self.driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/input').click()
        time.sleep(5)
    def test_denglu02(self):
        self.driver.get("http://192.168.1.251/bsams/front/login.do")
        self.driver.find_elements_by_tag_name("input")[0].send_keys("77")
        self.driver.find_elements_by_tag_name("input")[1].send_keys("student1")
        self.driver.find_elements_by_tag_name("input")[2].send_keys("student1")
        self.driver.find_elements_by_tag_name("input")[3].send_keys("shtd")
        self.driver.find_element_by_xpath('//*[@id="fmedit"]/div[2]/div[6]/input').click()
        self.driver.find_element_by_link_text('供应商').click()
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()