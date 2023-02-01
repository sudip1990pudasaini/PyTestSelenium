from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
This class is the main class (parent class)
It contains all generic methods and utilities for all other pages
"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        element.click()

    def insert_text(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        element.send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        return element.text

    def is_element_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        return bool(element)

    def get_page_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_elements(self, by_locator):
        try:
            return self.driver.find_elements(By.XPATH, by_locator)
        except NoSuchElementException:
            assert False

    def select_value_from_dropdown(self, by_locator, value):
        select = Select(self.driver.find_element(By.XPATH, by_locator))
        select.select_by_value(value)
