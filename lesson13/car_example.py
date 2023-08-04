from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self, wheels, color, fuel_type):
        self.wheels = wheels
        self.color = color
        self.fuel_type = fuel_type

    @abstractmethod
    def go_straight(self):
        pass

    @abstractmethod
    def refuel(self):
        pass
        @staticmethod
        def open_window():
            print("Window has opened")

class ElectroCar:
    def __init__(self, wheels, color, fuel_type):
        super().__init__(wheels, color, fuel_type)

        @staticmethod
        def go_straight():
            print(" car going straight ")

        def refuel(self):
            print("Car charged")

class Gasoline(Car):
    def __init__(self, wheels, color, fuel_type):
        super().__init__(wheels, color, fuel_type)

    def go_straight(self):
        print("going straight")

    def refuel(self):
        print("Car fuelled")


