import time

from selenium.webdriver.common.by import By

from pages import LoginPage
from pages.LoginPage import LOGINPAGE
from common.logger import logger

def test_SMP_lohin_001():

    logger.info("进入用例1")
    loginUI = LOGINPAGE()
    logger.info("输入密码")
    loginUI.login('byhy','sdfsdf')

    time.sleep(1)

    nav = loginUI.wd.find_element(By.TAG_NAME,'nav')

    assert nav!=[]