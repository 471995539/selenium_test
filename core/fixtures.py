'''

'''
from os import name
# from .init import init
import password as password
from po.pages import dbshop_index_page, dbshop_login_page

def dbshop_login(driver,name,password):
    '''
    登录函数
    :param driver:
    :param name:
    :param password:
    :return:
    '''
    index_po = dbshop_index_page(driver)
    login_po = dbshop_login_page(driver)
    index_po.get_login_link().click()



