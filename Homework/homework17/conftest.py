'''
Выберите любой сайт. повторите сделанное на лекции для него. Реализуйте инстанцирование драйвера через фикстуру,
Реализуйте пейдж обжекты, добавьте базовые элементы типа клика мыши, сэнд кейс в базовом классе. Напишите 5-10 тестов
(можете больше)
'''
from selenium.webdriver import Chrome
from Homework.homework17.pages.main_page_touch import MainPage
from Homework.homework17.pages.apple_page import ApplePage
from Homework.homework17.pages.xiaomi_page import XiaomiPage
import pytest


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()

    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture
def main_page(driver):
    driver.get('https://touch.com.ua/')
    yield MainPage(driver)


@pytest.fixture
def apple_page(driver):
    driver.get('https://touch.com.ua/tekhnika-apple/')
    yield ApplePage(driver)


@pytest.fixture
def xiaomi_page(driver):
    driver.get('https://touch.com.ua/tekhnika-xiaomi/')
    yield XiaomiPage(driver)
