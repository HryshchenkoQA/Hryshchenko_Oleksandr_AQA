import time


from Homework.homework17.conftest import main_page, driver

def test01_go_to_sales_and_discount(main_page):
    main_page.go_to_sales_and_discounts()
    time.sleep(3)

def test02_go_to_cart(main_page):
    main_page.go_to_cart_page()
    time.sleep(3)

def test03_go_to_apple_gadgets(main_page):
    main_page.go_to_apple_gadgets()
    time.sleep(3)

def test04_click_to_finder(main_page):
    main_page.click_to_finder()
    time.sleep(3)
