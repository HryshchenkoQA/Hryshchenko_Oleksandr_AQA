'''
Абстрактаная машина и конкретные машины.
Описание машины с абстрактными методами (ехать, стоп) и
описание машин по виду топлива (дизель, газ, бензин,
электро, гибрид)
'''
from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self, body_type, fuel_type, convertible):
        self.body_type = body_type
        self.fuel_type = fuel_type
        self.convertible = convertible

    @abstractmethod
    def drive_forward(self):
        pass

    @abstractmethod
    def drive_back(self):
        pass


    def refuel(self):
        pass


    def open_window(self):
        print("window has opened")

class ElectroCar(Car):
    def __init__(self, body_type, fuel_type, convertible):
        super().__init__(body_type, fuel_type, convertible)

    def drive_forward(self):
        print("the car goes forward")

    def drive_back(self):
        print("the car is going backwards")

    def refuel(self):
        print('Car is charged')

class Gasoline(Car):
    def __init__(self, body_type, fuel_type, convertible):
        super().__init__(body_type, fuel_type, convertible)

    def drive_forward(self):
        print("the car goes forward")

    def drive_back(self):
        print("the car is going backwards")

    def refuel(self):
        print('Car is fueled')

mini_cooper = Gasoline("sedan", "gasoline", "yes")
tesla = ElectroCar("crossover", "electro", "no")
mini_cooper.drive_forward()
mini_cooper.drive_back()

tesla.drive_forward()
tesla.drive_back()

print(mini_cooper.fuel_type)
print(tesla.fuel_type)

mini_cooper.open_window()
tesla.open_window()
