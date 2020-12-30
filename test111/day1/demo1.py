'''

'''
import unittest
from selenium import webdriver
import time

from core.init import init

driver = init("http://116.85.42.10/")

driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("user_name").send_keys("test1")
driver.find_element_by_id("user_password").send_keys("123456")
driver.find_element_by_xpath("//*/div/button[1]").click()
#随机选择一个商品
driver.find_element_by_xpath("//*/div/button/span").click()
time.sleep(2)
driver.find_element_by_id("J_miniCart").click()
time.sleep(2)
driver.find_element_by_link_text("去结算").click()
# driver.find_element_by_xpath("//*[@id=\"cart_step\"]/label[1]").click()
# driver.back()#返回
time.sleep(3)
driver.refresh()
driver.quit()
time.sleep(3)