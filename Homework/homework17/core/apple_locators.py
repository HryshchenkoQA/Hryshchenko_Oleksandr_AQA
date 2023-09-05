from Homework.homework17.core.base_locators import BaseLocator


class AppleLocators(BaseLocator):
    def __init__(self):
        super().__init__()
        self.iphone = ('xpath', '//*[@id="right"]/div[2]/div[1]/div[1]/a/div[2]')
        self.airpods = ('xpath', '//*[@id="right"]/div[2]/div[1]/div[2]/a/div[2]')
        self.ipad = ('xpath', '//*[@id="right"]/div[2]/div[1]/div[4]/a/div[2]')
        self.macbook = ('xpath', '//*[@id="right"]/div[2]/div[1]/div[5]/a/div[2]')
