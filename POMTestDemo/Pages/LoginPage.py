from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage
from Pages.BasePage import BasePage
from Config.config import TestData

class LoginPage(BasePage):
    EMAIL =(By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT,"Get started free")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    
    def get_login_page_title(self, title):
        return self.get_title(title)
    
    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)
    
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)
    