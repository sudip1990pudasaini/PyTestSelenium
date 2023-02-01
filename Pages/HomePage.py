from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage
from Pages.ItemDetailsPage import ItemDetailsPage


class HomePage(BasePage):
    """Home Page Elements"""
    HEADER = ("xpath", "//*[@class='title']")
    PRODUCT_FILTER = ("xpath", "//*[@class='select_container']")
    PEEK_ICON = ("xpath", "//*[@class='peek']")
    CART_ICON = ("xpath", "//*[@class='shopping_cart_link']")
    COUNT_ON_CART_ICON = ("xpath", "//*[@class='shopping_cart_badge']")

    INVENTORY_ITEM = "//*[@class='inventory_item']"
    INVENTORY_ITEM_NAME = "//*[@class='inventory_item_name']"

    PRODUCT_SORT_CONTAINER = "//*[@class='product_sort_container']"
    SORTING_Z_TO_A = "za"

    """Constructor of Page Class"""

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_page_title(title)

    def is_peek_icon_exists(self):
        return self.is_element_visible(self.PEEK_ICON)

    def get_header_value(self):
        if self.is_element_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def is_sort_container_exists(self):
        return self.is_element_visible(self.PRODUCT_FILTER)

    def click_on_sort_container(self):
        self.click_element(self.PRODUCT_FILTER)

    def is_cart_icon_exists(self):
        return self.is_element_visible(self.CART_ICON)

    def is_count_on_cart_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.COUNT_ON_CART_ICON)
            )
            not_found = False
        except NoSuchElementException:
            not_found = True
        assert not_found

    def get_count_on_cart_value(self):
        if self.is_element_visible(self.COUNT_ON_CART_ICON):
            return self.get_element_text(self.COUNT_ON_CART_ICON)

    def count_items_on_home_page(self):
        elements = self.get_elements(self.INVENTORY_ITEM)
        return len(elements)

    def list_of_items(self):
        elements = self.get_elements(self.INVENTORY_ITEM_NAME)
        lst = []
        for e in elements:
            item = e.text
            lst.append(item)
        return lst

    def select_specific_element(self, item_name=""):
        elements = self.get_elements(self.INVENTORY_ITEM_NAME)
        for e in elements:
            item = e.text
            if item == item_name:
                e.click()
                break
            else:
                return False
        return ItemDetailsPage(self.driver)

    def sort_items_by_z_to_a(self):
        self.select_value_from_dropdown(self.PRODUCT_SORT_CONTAINER, self.SORTING_Z_TO_A)
