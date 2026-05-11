from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from common.logger import logger

class BASEPAGE():
    def __init__(self):
        logger.info("浏览器打开")
        options = Options()
        # 关闭 Chrome 的密码管理功能（两套）
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "autofill.profile_enabled": False,
            "autofill.address_enabled": False,
            "autofill.credit_card_enabled": False,
        })

        # 关闭保存密码弹窗（这一条非常关键）
        options.add_argument("--disable-save-password-bubble")

        # 同时关闭另一个密码管理器（Google Smart Lock）
        options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordLeakDetection")

        # 关闭所有提示气泡，否则仍会出现遮挡
        options.add_argument("--disable-infobars")

        # 禁用自动填充（否则 Chrome 会认为你在输入密码）
        options.add_argument("--disable-autofill-keyboard-accessory-view")
        options.add_argument("--disable-autofill")
        options.add_argument("--disable-browser-autofill")
        # 可选但推荐：无痕模式减少弹窗
        options.add_argument("--incognito")

        self.wd = webdriver.Chrome(options=options)
        self.wd.implicitly_wait(10)