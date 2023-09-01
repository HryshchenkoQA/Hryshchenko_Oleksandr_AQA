import time
from lesson20.conftest import dashboard, driver


def test01_go_to_comics_and_books(dashboard):
    dashboard.go_to_comics_and_books()
    time.sleep(5)


def test02_go_to_loign_form(dashboard):
    dashboard.go_to_login_form()
    time.sleep(5)


def test03_search_for_pathfinder(dashboard):
    dashboard.search_for_game('pathfinder')
    time.sleep(5)
