import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=Service(TestData.EXECUTABLE_PATH))
    web_driver.get(TestData.BASE_URL)
    request.cls.driver = web_driver

    yield
    web_driver.close()
