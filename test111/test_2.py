import time
import unittest
import json

from ddt import ddt, data
from selenium import webdriver

with open("test_data.json", "rt", encoding="utf-8") as fp:
    test_data = json.load(fp)

# print(test_data)

class TestAdd(unittest.TestCase):
    def test_01(self):

        self.assertEqual(1, 1, "fail")

    pass

@ddt
class TestDbshoplogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="D:\web_zidonghua\drivers\chromedriver.exe")

        self.driver.get("http://116.85.42.10")

        time.sleep(3)


    def test_01(self):

        pass




    # assert isinstance(test_data, )

    @data(*test_data)
    def test_1(self, test_name, test_password, exptected="test1"):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("user_name").send_keys("test_name")
        self.driver.find_element_by_id("user_password").send_keys("test_password")
        self.driver.find_element_by_xpath("//button[@type='submit']").submit()
        a = self.driver.find_element_by_link_text("test1")
        self.assertIn(a.test,exptected,"登录不成功")


    def tearDown(self) -> None:
        self.driver.quit()
