from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import TestData

class Test_Home(BaseTest):
    
    def test_home_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        homePage = self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title==TestData.HOME_PAGE_TITLE
    
    def test_home_page_header(self):
        self.LoginPage = LoginPage(self.driver)
        homePage = self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = homePage.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER
    
    def test_home_page_account(self):
        self.LoginPage = LoginPage(self.driver)
        homePage = self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        account_name = homePage.get_account_name_value()
        assert account_name == TestData.ACCOUNT_NAME
    
    def test_settings_icon(self):
        self.LoginPage = LoginPage(self.driver)
        homePage = self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert homePage.is_settings_icon_exist()
        
        
	