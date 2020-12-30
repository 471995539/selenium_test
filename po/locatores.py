'''

'''
from selenium.webdriver.common.by import By

class dbbshop_index_page_locatores(object):
    LOGIN_LINK = (By.LINK_TEXT,"登录")
    CHOOSE_GOODS = (By.XPATH, "//*/div/button/span")
    GOODS_ADDCAT = (By.ID, "J_miniCart")
class dbshop_login_page_locatores(object):
    USER_NAME = (By.ID, "user_name")
    USER_PASSWORD = (By.ID, "user_password")
    LOGIN_SUBMIT = (By.XPATH,"//button[@type='submit']")

# class dbshop_choose_goods_locatores(object):
#     CHOOSE_GOODS = (By.XPATH,"//*/div/button/span")

# class dbshop_goods_addcat_locatores(object):
#     GOODS_ADDCAT = (By.ID,"J_miniCart")

class dbshop_goods_balance_locatores(object):
    GOODS_BALANCE = (By.LINK_TEXT,"去结算")




