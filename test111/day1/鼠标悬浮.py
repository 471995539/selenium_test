'''
#鼠标悬浮和断言页面是否包含某些字体信息
'''
import unittest

from selenium.webdriver.common.by import By

import core


class TestDbshopHomePage(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = core.init()
        self.driver.get("http://localhost/dbshop/")

    def test_01(self):
        '''
        测试首页有用户中心连接
        :return:
        '''
        test_data = "用户中心"
        element = self.driver.find_element(By.LINK_TEXT,test_data)
        flag = False
        if element.is_displayed():
            flag = True
        self.assertTrue(flag)
        pass
    def test_02(self):
        '''
        测试首页标题包含“”
        :return:
        '''



    def tearDown(self) -> None:
        self.driver.quit()