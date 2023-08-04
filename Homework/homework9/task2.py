'''
Создайте класс с описанием любой компании или организации. Добавьте 1 classmethod, 3 обычных метода
'''

class Apple:
    def __init__(self, name, location, employees):
        self.name = name
        self.location = location
        self.employees = employees

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_employees(self):
        return self.employees

    @classmethod
    def create_apple(cls):
        return cls("Apple", "Cupertino, CA", 154.000)

    def sell_iphone(self):
        print("iPhone sold!")

    def sell_macbook(self):
        print("MacBook sold!")

    def sell_ipad(self):
        print("iPad sold!")
apple = Apple.create_apple()

print(apple.get_name())
print(apple.get_location())
print(apple.get_employees())

apple.sell_iphone()
apple.sell_macbook()
apple.sell_ipad()
