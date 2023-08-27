'''
Выберите любой интернет ресурс. напишите 5 любых простых тестов на нажатие на элементы и ввод текста.
*необязательная задача. добавьте проверки с помощью assert. Пройдитесь по пагинации. Отфильтруйте вывод (например,
введите в фильтре на сайте минимальную или максимальную цену)
'''
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_01_find_cyberpunk():
    driver = Chrome()
    driver.get("https://store.steampowered.com/")
    search_field_locator = '//*[@id="store_nav_search_term"]'
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys("Cyberpunk 2077")
    element.send_keys(Keys.ENTER)
    time.sleep(5)

#good morning night city (:

def test_02_find_iphone():
    driver = Chrome()
    driver.get("https://rozetka.com.ua/ua")
    search_locator = '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div[1]/input'
    search = driver.find_element(by='xpath', value=search_locator)
    search.send_keys("Iphone 14 deep purple")
    search.send_keys(Keys.ENTER)
    time.sleep(5)

def test_03_choice_iphone(): #not max
    driver = Chrome()
    driver.get("https://rozetka.com.ua/ua/search/?text=iphone+14+deep+purple")
    find_iphone_locator = '/html/body/app-root/div/div/rz-search/rz-catalog/div/div[2]/section/rz-grid/ul/li[2]/rz-catalog-tile/app-goods-tile-default/div/div[2]'
    find_iphone = driver.find_element(by='xpath', value=find_iphone_locator)
    find_iphone.click()
    time.sleep(5)

def test_04_check_price():
    driver = Chrome()
    driver.get("https://rozetka.com.ua/ua/apple-iphone-14-pro-128gb-deep-purple/p352490706/")
    find_price_locator = '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/div[1]/div[1]/div[1]/p[2]'
    find_price = driver.find_element(by='xpath', value=find_price_locator)
    print(f"Price on iPhone 14 pro Deep Purple is {find_price.text}")
    time.sleep(5)

# def test_05_check_iphone_color():
#     driver = Chrome()
#     driver.get("https://rozetka.com.ua/ua/apple-iphone-14-pro-128gb-deep-purple/p352490706/")
#     check_color_locator = '//p[@class="var-options__label"]/text()'
#     check_color = driver.find_element(by='xpath', value=check_color_locator)
#     assert check_color.text == "Purple"
#     time.sleep(5)


def test_05_check_price_forza_horizon_5():
    driver = Chrome()
    driver.get("https://store.steampowered.com/app/1551360/Forza_Horizon_5")
   # price_locator = '//*[@class ="game_purchase_price price"]'
    price_locator = '//*[@class= "discount_final_price"]'
    price = driver.find_element(by='xpath', value=price_locator)
    print(f"Price on Forza Horizon 5 is {price.text}")
    time.sleep(5)





