from Homework.homework17.core.apple_locators import AppleLocators
from Homework.homework17.pages.base_page_touch import BasePage


class ApplePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AppleLocators()

    def go_to_iphones(self):
        self.click_on_element(self.locators.iphone)

    def go_to_airpods(self):
        self.click_on_element(self.locators.airpods)

    def go_to_ipads(self):
        self.click_on_element(self.locators.ipad)

    def go_to_macbooks(self):
        self.click_on_element(self.locators.macbook)
