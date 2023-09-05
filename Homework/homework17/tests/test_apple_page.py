from Homework.homework17.conftest import apple_page, driver

import time


def test01_transition_iphone_page(apple_page):
    apple_page.go_to_iphones()
    time.sleep(5)


def test02_transition_airpods_page(apple_page):
    apple_page.go_to_airpods()
    time.sleep(5)


def test03_transition_macbooks_page(apple_page):
    apple_page.go_to_macbooks()
    time.sleep(5)


def test04_transition_ipads_page(apple_page):
    apple_page.go_to_ipads()
    time.sleep(5)
