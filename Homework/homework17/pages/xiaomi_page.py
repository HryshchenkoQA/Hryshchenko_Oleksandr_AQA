from Homework.homework17.core.xiaomi_locators import XiaomiLocators
from Homework.homework17.pages.base_page_touch import BasePage


class XiaomiPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = XiaomiLocators()

    def go_to_phones(self):
        self.click_on_element(self.locators.xiaomi_phones)

    def go_to_tables(self):
        self.click_on_element(self.locators.xiaomi_tablets)

    def go_to_notebooks(self):
        self.click_on_element(self.locators.xiaomi_notebooks)
