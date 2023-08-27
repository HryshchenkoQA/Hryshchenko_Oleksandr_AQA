from selenium.webdriver import Chrome
from lesson20.pages.dashbord_page import Dashbord
import pytest

from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.get('https://touch.com.ua')
    driver.maximize_window()

    yield driver
    driver.close()



@pytest.fixture()
def dashboard(driver):
    yield Dashbord(driver)

