from selenium.webdriver import Chrome
from lesson20.pages.dashbord_page import Dashbord
import pytest

from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture
def dashboard(driver):
    driver.get('https://lordofboards.com.ua/')

    yield Dashbord(driver)
