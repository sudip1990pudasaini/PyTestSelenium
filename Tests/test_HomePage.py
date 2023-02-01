from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.test_base import BaseTest


class TestHomePage(BaseTest):

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        title = home_page.get_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        header = home_page.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER

    def test_cart_icon_exists(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        is_exists = home_page.is_cart_icon_exists()
        assert is_exists

    def test_count_on_cart_icon_exists(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        is_exists = home_page.is_count_on_cart_displayed()
        assert not is_exists

    def test_peek_icon_exists(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        is_exists = home_page.is_peek_icon_exists()
        assert is_exists

    def test_sort_container_exists(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        is_exists = home_page.is_sort_container_exists()
        assert is_exists

    def test_items_count_on_home_page(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        count = home_page.count_items_on_home_page()
        assert count == 6

    def test_items_sorting_on_home_page(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        items = home_page.list_of_items()
        assert items == TestData.HOME_PAGE_ITEMS_A_TO_Z


"""This class is for adding and removing items in the cart"""


class TestSortList(BaseTest):

    def test_sort_z_to_a(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)

        is_exists = home_page.is_sort_container_exists()
        assert is_exists

        home_page.sort_items_by_z_to_a()
        items = home_page.list_of_items()
        assert items != TestData.HOME_PAGE_ITEMS_A_TO_Z

        items.reverse()
        assert items == TestData.HOME_PAGE_ITEMS_A_TO_Z

