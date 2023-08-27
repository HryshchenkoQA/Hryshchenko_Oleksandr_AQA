from Homework.homework17.pages.base_page_touch import BasePage




class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_sales_and_discounts(self):
        locator = ('xpath', '//*[@id="subMenu"]/li[1]')
        element = self.wait_until_element_appears(locator)
        element.click()

    def go_to_cart_page(self):
        locator = ('xpath', '//span[@class="cartLabel"]')
        element = self.wait_until_element_appears(locator)
        element.click()

    def go_to_apple_gadgets(self):
        locator = ('xpath', '//input[@id="searchQuery"]')
        element = self.wait_until_element_appears(locator)
        element.click()

    def click_to_finder(self):
        locator = ('//*[@id="searchQuery"]')
        element = self.wait_until_element_appears(locator)
        element.click()





