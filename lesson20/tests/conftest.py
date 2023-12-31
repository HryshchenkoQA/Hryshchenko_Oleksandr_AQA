from selenium.webdriver import Chrome  # импортируем хром
from lesson20.pages.dashboard_page import Dashboard
from lesson20.pages.category_page import CategoryPage
import pytest


@pytest.fixture(scope='session')
def driver():  # фикстура драйвера, которая создает драйвер
    driver = Chrome()
    driver.maximize_window()

    yield driver  # возвращает драйвер
    driver.close()


@pytest.fixture
def dashboard(driver):  # наследуемся с драйвера, открываем главную страницу. генераторная функция
    driver.get('https://lordofboards.com.ua/')  # вызов конкретной страницы

    yield Dashboard(driver)


@pytest.fixture
def categories(driver):  # наследуемся с драйвера, открываем категорию. Объявляем функцию
    driver.get('https://lordofboards.com.ua/komiksy-i-knigi/')  # открываем категорию

    driver.add_cookie({'name': 'flag', 'value': 'red'})
    print(f'coockie: {driver.get_cookie("flag")}')
    driver.execute_script("window.localStorage['flag1']= 'green' ")
    print(driver.execute_script("return window.localStorage['flag1'];"))
    yield CategoryPage(driver)
