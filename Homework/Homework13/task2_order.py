from abc import abstractmethod

class Dish():

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

class OrderPart:

    def __init__(self, dish):
        self.dish = dish

    def get_dish(self):
        return self.dish



class Risotto(Dish):

    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class Pasta(Dish):

    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Pizza(Dish):

    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

order_part = OrderPart(Risotto("Risotto with mushrooms", 15))
print(order_part.get_dish().get_name())

order_part = OrderPart(Pasta("Spaghetti with tomato sauce", 10))
print(order_part.get_dish().get_name())

order_part = OrderPart(Pizza("Margherita pizza", 20))
print(order_part.get_dish().get_name())