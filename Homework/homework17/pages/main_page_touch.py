from Homework.homework17.pages.base_page_touch import BasePage




class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_sales_and_discounts(self):
        locator = ('xpath', '//*[@id="subMenu"]/li[1]')
        self.click_on_element(locator)

    def go_to_cart_page(self):
        locator = ('xpath', '//span[@class="cartLabel"]')
        self.click_on_element(locator)

    def go_to_apple_gadgets(self):
        locator = ('xpath', '//input[@id="searchQuery"]')
        self.click_on_element(locator)

    def click_to_finder(self):
        locator = ('xpath', '//*[@id="searchQuery"]')
        self.click_on_element(locator)

    def find_iphone(self, message):
        locator = ('xpath', '//*[@id="searchQuery"]')
        self.send_keys_intro_field(locator, message)
        self.press_enter(locator)

