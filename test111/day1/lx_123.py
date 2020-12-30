import unittest
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.126.com/")
driver.maximize_window()


driver.find_element_by_name("email").send_keys("li471995539")
time.sleep(1)
driver.find_element_by_name("password").send_keys("li123456")
time.sleep(1)
driver.find_element_by_id("dologin").click()
time.sleep(1)
driver.quit()
time.sleep(3)