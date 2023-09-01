import time

from lesson20.pages.base_page import BasePage


class Dashbord(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_comics_and_books(self):
        locator = ('xpath', '/html/body/div[2]/div[1]/div/div[3]/div/div/div/div/div/ul/li[1]/div[1]/a')
        self.click_on_element(locator)

    def go_to_login_form(self):
        locator = ('xpath', '/html/body/div[2]/div[1]/div/div[2]/div/div/div[3]/div[1]/div/div/a')
        self.click_on_element(locator)

    def search_for_game(self, message):
        search_input_locator = ('xpath', '//input[@class="search__input"]')
        first_result_element_locator = ('xpath', '//div[@class="search-results__title"]')
        self.send_keys_intro_field(search_input_locator, message)
        self.wait_until_element_appears(first_result_element_locator)
        # time.sleep(5)
        self.press_enter(search_input_locator)
