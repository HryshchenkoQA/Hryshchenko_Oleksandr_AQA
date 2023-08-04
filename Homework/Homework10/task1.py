'''
Опишите класс любого транспортного средства.
Воспользуйтесь двумя уровнями наследования и абстракцией с помощью ABC(использование ABC не считается
за уровень наследования)
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        """Метод, который управляет транспортным средством."""

    @abstractmethod
    def stop(self):
        """Метод, который останавливает транспортное средство."""

class Engine(ABC):

    @abstractmethod
    def start(self):
        """Метод, который запускает двигатель."""

    @abstractmethod
    def stop(self):
        """Метод, который останавливает двигатель."""

class GasolineEngine(Engine):

    def start(self):
        print("Бензиновый двигатель запускается.")

    def stop(self):
        print("Бензиновый двигатель останавливается.")

class DieselEngine(Engine):

    def start(self):
        print("Дизельный двигатель запускается.")

    def stop(self):
        print("Дизельный двигатель останавливается.")

class Car(Vehicle):

    def __init__(self, engine: Engine, bodystyle: str):
        self.engine = engine
        self.bodystyle = bodystyle

    def drive(self):
        print(f"Автомобиль с {self.bodystyle} кузовом едет.")

    def stop(self):
        print(f"Автомобиль с {self.bodystyle} кузовом останавливается.")

class Sedan(Car):

    def __init__(self, engine: Engine):
        super().__init__(engine, "седан")

class SUV(Car):

    def __init__(self, engine: Engine):
        super().__init__(engine, "внедорожник")

