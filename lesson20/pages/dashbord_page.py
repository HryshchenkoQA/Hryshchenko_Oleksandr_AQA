from lesson20.pages.base_page import BasePage


class Dashbord(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_sales_and_discounts(self):
        locator = ('xpath', '//*[@id="subMenu"]/li[1]')
        element = self.wait_until_element_appears(locator)
        element.click()

    def go_to_cart_page(self):
        locator = ('xpath', '//span[@class="cartLabel"]')
        element = self.wait_until_element_appears(('xpath', '//span[@class="cartLabel"]'))
        element.click()

