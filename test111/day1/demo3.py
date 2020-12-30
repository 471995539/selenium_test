'''
使用显示和隐式等待
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("http://116.85.42.10/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("user_name").send_keys("test1")
driver.find_element_by_id("user_password").send_keys("123456")
driver.find_element_by_xpath("//*/div/button[1]").click()
#点击图片链接
driver.find_element_by_xpath("//*[@id=\"floor_1\"]/div[2]/div[2]/div/div[1]/div/a/img").click()
driver.find_element_by_id("add_cart_submit").click()

a =driver.find_element_by_class_name("btn btn-primary")
# element = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.,‘a’)))
element = WebDriverWait(driver, 10, 1).until(lambda x: x.a)
element.click()


driver.find_element_by_link_text("去结算").click()
# driver.find_element_by_xpath("//*[@id=\"cart_step\"]/label[1]").click()
# driver.back()#返回
time.sleep(3)
driver.refresh()
driver.quit()
time.sleep(3)