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
        locator = ('xpath', '//input[@class="search__input"]')
        self.send_keys_intro_field(locator, message)
        self.press_enter(locator)
