import time
import unittest
import json

from ddt import ddt, data
from selenium import webdriver

# with open("test_data_login.json", "rt", encoding="utf-8") as fp:
#     test_data = json.load(fp)

# print(test_data)
from selenium.webdriver.common.by import By

from core.fixtures import dbshop_login
from core.init import init
from po.pages import dbshop_index_page, dbshop_login_page


class TestDbshoplogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = init("http://localhost/dbshop/")

        self.dbshop_index_page = dbshop_index_page(self.driver)#调用登录页面
        self.dbshop_login_page = dbshop_login_page(self.driver)
    def test_1(self):
        test_name = "test1"
        test_password = "123456"

        # self.driver.find_element(By.LINK_TEXT, "登录").click()
        # 点击登录连接
        self.dbshop_index_page.click_login_link()
        # 输入用户名和密码。点击登录按钮
        self.dbshop_login_page.login_action(test_name, test_password)
        # self.driver.find_element(By.ID, "user_name").send_keys(test_name)
        # self.driver.find_element(By.ID, "user_password").send_keys(test_password)
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").submit()
        # dbshop_login(self.driver, test_name,test_password)
        a = self.driver.find_element_by_link_text(test_name)
        self.assertIn(a.text, test_name, "登录不成功")

    def tearDown(self) -> None:
        self.driver.quit()
