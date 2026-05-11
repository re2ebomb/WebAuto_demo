from robot.libraries.String import String
from selenium.webdriver.common.by import By
import time

from common import BasePage
from common.BasePage import BASEPAGE
from common.logger import logger
from common.read_yaml import  *



class LOGINPAGE(BASEPAGE):

    def login(self,username,password):
        logger.info("进入登录页面")

        logger.info(login_url)
        self.wd.get(login_url)
       # time.sleep(1)
        if username is not None:
            self.wd.find_element(By.ID,'username').send_keys(username)
        if password is not None:
            self.wd.find_element(By.ID,'password').send_keys(password)
       # time.sleep(1)
        self.wd.find_element(By.ID,'loginBtn').click()
        time.sleep(1)