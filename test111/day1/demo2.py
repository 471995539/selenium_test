#driver.refresh()刷新
import unittest
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://116.85.42.10/")
driver.maximize_window()
for i in range(11):
    time.sleep(1)
    driver.refresh()
driver.quit()

