
class BaseLocator:
    def __init__(self):
        self.adv = ('xpath', '//ul[@id="subMenu"]/li[1]/a')
        self.credit = ('xpath', '//ul[@id="subMenu"]/li[2]/a')
        self.delivery_and_payment = ('xpath', '//ul[@id="subMenu"]/li[3]/a')
