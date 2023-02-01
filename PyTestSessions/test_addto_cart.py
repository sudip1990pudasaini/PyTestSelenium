from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestAddToCart(BaseTest):

    def test_select_first_item(self):
        valid_username = "standard_user"
        valid_password = "secret_sauce"

        self.driver.find_element("id", "user-name").send_keys(valid_username)
        self.driver.find_element("id", "password").send_keys(valid_password)
        self.driver.find_element("id", "login-button").click()

        self.driver.find_element("xpath", "//*[@class='title']").is_displayed()
        title_text = self.driver.find_element("xpath", "//*[@class='title']").text

        assert title_text == "PRODUCTS"

        item_elements = self.driver.find_elements("xpath", "//*[@class='inventory_item_name']")
        item_name = [el.text for el in item_elements]

        for text in item_name:
            if text == "Sauce Labs Backpack":
                self.driver.find_element("xpath", "//*[@class='inventory_item_name']").click()
                try:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(("xpath", "//*[@class='inventory_details_name large_size']"))
                    )
                except NoSuchElementException:
                    assert False
                assert True

    def test_add_item_to_cart(self):
        valid_username = "standard_user"
        valid_password = "secret_sauce"

        self.driver.find_element("id", "user-name").send_keys(valid_username)
        self.driver.find_element("id", "password").send_keys(valid_password)
        self.driver.find_element("id", "login-button").click()

        self.driver.find_element("xpath", "//*[@class='title']").is_displayed()
        title_text = self.driver.find_element("xpath", "//*[@class='title']").text

        assert title_text == "PRODUCTS"

        add_to_cart_btn = self.driver.find_element("id", "add-to-cart-sauce-labs-backpack")
        cart_link = self.driver.find_element("xpath", "//*[@class='shopping_cart_link']")

        add_to_cart_btn.click()
        cart_link.click()

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", "remove-sauce-labs-backpack"))
            )
        except NoSuchElementException:
            assert False
        assert True
