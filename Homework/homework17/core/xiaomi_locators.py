from Homework.homework17.core.base_locators import BaseLocator


class XiaomiLocators(BaseLocator):
    def __init__(self):
        super().__init__()
        self.xiaomi = ('xpath', '//*[@id="leftMenu"]/li[3]/a')
        self.xiaomi_phones = ('xpath', '//*[@id="right"]/div[2]/div[1]/div[1]/a/div[2]')
        self.xiaomi_tablets = ('xpath', '//*[@id="right"]/div[2]/div[1]/div[2]/a/div[2]')
        self.xiaomi_notebooks = ('xpath', '//*[@id="right"]/div[2]/div[1]/div[6]/a/div[2]')
