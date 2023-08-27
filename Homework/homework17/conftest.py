'''
Выберите любой сайт. повторите сделанное на лекции для него. Реализуйте инстанцирование драйвера через фикстуру,
Реализуйте пейдж обжекты, добавьте базовые элементы типа клика мыши, сэнд кейс в базовом классе. Напишите 5-10 тестов
(можете больше)
'''
from selenium.webdriver import Chrome
from Homework.homework17.pages.main_page_touch import MainPage
import pytest


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.get('https://touch.com.ua/')
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture()
def main_page(driver):
    yield MainPage(driver)
