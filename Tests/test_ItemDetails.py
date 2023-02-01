from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.test_base import BaseTest


class TestHomePage(BaseTest):

    def test_details_page_title(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        details_page = home_page.select_specific_element(TestData.HOME_PAGE_ITEMS_A_TO_Z[0])
        title = details_page.get_details_page_title(TestData.DETAILS_PAGE_TITLE)
        assert title == TestData.DETAILS_PAGE_TITLE

    def test_item_description(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        details_page = home_page.select_specific_element(TestData.HOME_PAGE_ITEMS_A_TO_Z[0])
        description = details_page.get_item_description()
        assert description == TestData.ITEM_DESCRIPTION

    def test_add_item_to_cart(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        details_page = home_page.select_specific_element(TestData.HOME_PAGE_ITEMS_A_TO_Z[0])
        details_page.click_add_to_cart_button()
        is_exists = details_page.is_remove_button_visible()

        assert is_exists

    def test_counter_displayed_on_cart(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        details_page = home_page.select_specific_element(TestData.HOME_PAGE_ITEMS_A_TO_Z[0])
        details_page.click_add_to_cart_button()
        is_exists = home_page.is_count_on_cart_displayed()
        if is_exists:
            count_value = home_page.get_count_on_cart_value()
            assert count_value == 1
