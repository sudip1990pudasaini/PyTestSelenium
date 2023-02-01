from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    """ By Locators"""
    LOGO = ("xpath", "//*[@class='login_logo']")
    USERNAME = ("id", "user-name")
    PASSWORD = ("id", "password")
    LOGIN_BTN = ("id", "login-button")

    """Constructor of Page Class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """Method to get page title"""
    def get_login_page_title(self, title):
        return self.get_page_title(title)

    """Method to check visibility of logo"""
    def is_logo_exists(self):
        return self.is_element_visible(self.LOGO)

    """Method to login"""
    def login(self, username, password):
        self.insert_text(self.USERNAME, username)
        self.insert_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BTN)
        return HomePage(self.driver)