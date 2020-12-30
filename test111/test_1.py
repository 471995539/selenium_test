import time
import unittest
import json

from selenium import webdriver

with open("test_data.json", "rt", encoding="utf-8") as fp:
    test_data = json.load(fp)

print(test_data)


import unittest


class TestAdd(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="D:\web_zidonghua\drivers\chromedriver.exe")

        self.driver.get("http://116.85.42.10")

        time.sleep(3)

    def test_01(self):

        self.assertEqual(1, 1, "fail")

    pass