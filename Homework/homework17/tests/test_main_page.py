import time


from Homework.homework17.conftest import main_page, driver

def test01_go_to_sales_and_discount(main_page):
    main_page.go_to_sales_and_discounts()
    time.sleep(5)



def test02_go_to_cart(main_page):
    main_page.go_to_cart_page()
    time.sleep(5)

def test03_go_credits(main_page):
    main_page.go_to_credits()
    time.sleep(5)

def test04_go_to_delivery(main_page):
    main_page.go_to_delivery()
    time.sleep(5)
