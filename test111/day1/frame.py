import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
a = driver.get("http://baidu.com")
driver.maximize_window()
action = ActionChains(driver)
action.move_by_offset()
driver.switch_to.frame(a)
driver.switch_to.default_content()


