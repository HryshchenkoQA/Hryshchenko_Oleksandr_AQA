from abc import abstractmethod
import pytest


class Dish:

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


@pytest.fixture
def risotto():
    return Risotto("Risotto with mushrooms", 15)


@pytest.fixture
def pasta():
    return Pasta("Spaghetti with tomato sauce", 10)


@pytest.fixture
def pizza():
    return Pizza("Margherita pizza", 20)


class TestOrderPart(object):

    def test_get_dish_name(self, risotto):
        order_part = OrderPart(risotto)
        assert order_part.get_dish().get_name() == "Risotto with mushrooms"

    def test_get_dish_price(self, risotto):
        order_part = OrderPart(risotto)
        assert order_part.get_dish().get_price() == 15

    def test_get_dish_name_pasta(self, pasta):
        order_part = OrderPart(pasta)
        assert order_part.get_dish().get_name() == "Spaghetti with tomato sauce"

    def test_get_dish_price_pasta(self, pasta):
        order_part = OrderPart(pasta)
        assert order_part.get_dish().get_price() == 10

    def test_get_dish_name_pizza(self, pizza):
        order_part = OrderPart(pizza)
        assert order_part.get_dish().get_name() == "Margherita pizza"

    def test_get_dish_price_pizza(self, pizza):
        order_part = OrderPart(pizza)
        assert order_part.get_dish().get_price() == 20


if __name__ == "__main__":
    pytest.main()
