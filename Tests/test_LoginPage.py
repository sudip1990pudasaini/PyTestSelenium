from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.test_base import BaseTest


class TestLogin(BaseTest):

    def test_logo_visible(self):
        self.loginPage = LoginPage(self.driver)
        is_exists = self.loginPage.is_logo_exists()
        assert is_exists

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)

