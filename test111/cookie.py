
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

test_name = "test1"

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.delete_all_cookies()
# 打开首页
driver.get("http://localhost/dbshop/home/useredit")
cookie_dict = {
    "name" :"PHPSESSID",
    "value" : "reesrgkiir3jkbe30pgeq9r696"
}
driver.add_cookie(cookie_dict=cookie_dict)
driver.refresh() #一定要有
# driver.find_element(By.LINK_TEXT, "登录").click()
#
# username = driver.find_element_by_id("user_name")
# password = driver.find_element_by_id("user_password")
# username.send_keys(test_name)
# password.send_keys("123456")
# driver.find_element_by_xpath("//button[@type='submit']").submit()

# 点击 登录名链接

driver.find_element(By.LINK_TEXT, test_name).click()
driver.find_element(By.NAME, "user_avatar").send_keys(r"D:\web_zidonghua\test111\laohu.jpg")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
driver.quit()  # 关闭所有窗口