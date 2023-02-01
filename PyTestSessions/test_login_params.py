import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestLoginParams(BaseTest):

    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("locked_out_user", "secret_sauce"),
            ("problem_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce")
        ]
    )
    def test_login_params(self, username, password):
        """
        This method is used to test login parameterized
        :param username:
        :param password:
        :return:
        """
        self.driver.find_element("id", "user-name").clear()
        self.driver.find_element("id", "user-name").send_keys(username)
        self.driver.find_element("id", "password").clear()
        self.driver.find_element("id", "password").send_keys(password)
        self.driver.find_element("id", "login-button").click()

        cart_icon = self.driver.find_element("xpath", "//*[@class='shopping_cart_container']")

        try:
            if cart_icon.is_displayed():
                # self.driver.back()
                self.driver.find_element("xpath", "//*[@class='bm-burger-button']").click()
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(("id", "logout_sidebar_link"))

                )
                self.driver.find_element("id", "logout_sidebar_link").click()
        except NoSuchElementException:
            assert False
        assert True
