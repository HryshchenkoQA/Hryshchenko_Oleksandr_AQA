from Homework.homework17.conftest import xiaomi_page, driver
import time

def test01_transition_phones_pages(xiaomi_page):
    xiaomi_page.go_to_phones()
    time.sleep(5)

def test02_transition_tables_page(xiaomi_page):
    xiaomi_page.go_to_tables()
    time.sleep(5)

def test03_transition_notebooks_page(xiaomi_page):
    xiaomi_page.go_to_notebooks()
    time.sleep(5)