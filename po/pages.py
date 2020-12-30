'''

'''
from selenium.webdriver.chrome.webdriver import WebDriver
from po.basePage import BasePage
from po.locatores import dbbshop_index_page_locatores, dbshop_login_page_locatores

class dbshop_index_page(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.locatores = dbbshop_index_page_locatores

    def get_login_link(self):
        '''
        点击登录连接并返回return
        :return:
        '''
        return self.driver.find_element(*self.locatores.LOGIN_LINK)
    def get_choose_goods_page(self):
        return self.driver.find_element(*self.locatores.CHOOSE_GOODS)
    def get_goods_addcat_page(self):
        return self.driver.find_element(*self.locatores.GOODS_ADDCAT)

    def click_login_link(self):

        el = self.get_login_link()
        el.click()

class dbshop_login_page(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

        self.locatores = dbshop_login_page_locatores

    def get_username_test_input_element(self):
        '''

        :return:
        '''
        return self.driver.find_element(*self.locatores.USER_NAME)
    def get_userpassword_test_input_element(self):
        '''

        :return:
        '''
        return self.driver.find_element(*self.locatores.USER_PASSWORD)
    def get_login_button_element(self):

        return self.driver.find_element(*self.locatores.LOGIN_SUBMIT)
    def get_choose_goods_page(self):

        return self.driver.find_element(*self.locatores.CHOOSE_GOODS)


    def  login_action(self, name , password):
        ''''
        登录动作
        '''


        self.get_username_test_input_element().send_keys(name)
        self.get_userpassword_test_input_element().send_keys(password)
        self.get_login_button_element().submit()
        pass



# class dbshop_choose_goods_page(BasePage):
#
#     def __init__(self, drver) -> None:
#         super().__init__(drver)
#         self.locatores = dbshop_login_page_locatores
#     def get_choose_goods_page(self):
#         return self.driver.find_element(*self.locatores.CHOOSE_GOODS)
# class dbshop_goods_addcat_page(BasePage):
#     def __init__(self, drver) -> None:
#         super().__init__(drver)
#         self.locatores = dbshop_goods_addcat_page
#     def get_goods_addcat_page(self):
#         return self.driver.find_element(*self.locatores.GOODS_ADDCAT)

class dbshop_goods_balance_page(BasePage):
    '''
    #结算页面
    '''
    def __init__(self, drver) -> None:
        super().__init__(drver)
        self.locatores = dbshop_goods_balance_page
    def get_goods_balance_page(self):
        return self.driver.find_element(*self.locatores.GOODS_BALANCE)




