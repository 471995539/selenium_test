'''
向套件中。增加用例。数据驱动的测试用例。不能单独加入套件
'''
import unittest
from core.HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover("tests", pattern='test_*.py')
    with open("reports.html", "wb") as fp:
        runner = HTMLTestRunner(stream=fp, title="测试报告", description="自动化测试结果", verbosity=3)
        runner.run(discover) # 使用runner去执行套件中的用例