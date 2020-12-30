import os

from selenium import webdriver


def init(url):
    '''
    初始化浏览器参数，并返回driver
    :return:
    '''
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "drivers", "chromedriver.exe"))
    driver = webdriver.Chrome(executable_path=path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url=url)
    return driver