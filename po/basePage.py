'''

'''
from selenium.webdriver.chrome.webdriver import WebDriver

class BasePage():
    def __init__(self, drver) -> None:
        self.driver = drver