from selenium.webdriver import Chrome
from lesson20.pages.dashbord_page import Dashbord
from lesson20.pages.category_page import CategoryPage
import pytest


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


@pytest.fixture
def categories(driver):
    driver.get('https://lordofboards.com.ua/komiksy-i-knigi/')
    yield CategoryPage(driver)
