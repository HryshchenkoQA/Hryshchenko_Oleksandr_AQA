class Train:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def __len__(self):
        return len(self.cars)

    def __str__(self):
        return f"Train {self.name} to {self.destination}"

class Person:
    def __init__(self, name, destination, place):
        self.name = name
        self.destination = destination
        self.place = place

    def __str__(self):
        return f"Person {self.name} is going to {self.destination} in seat {self.place}"

class TrainCar:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
        else:
            raise ValueError("The car is full.")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        passengers = [
            {
                "name": passenger.name,
                "destination": passenger.destination,
                "place": passenger.place,
            }
            for passenger in self.passengers
        ]
        return f"Car {self.number} with {len(passengers)} passengers: {passengers}"


train = Train("The Orient Express", "Paris to Istanbul")

car1 = TrainCar(1, 10)
car2 = TrainCar(2, 20)

train.add_car(car1)
train.add_car(car2)

passenger1 = Person("John Doe", "Paris", 1)
passenger2 = Person("Jane Doe", "Istanbul", 2)

car1.add_passenger(passenger1)
car2.add_passenger(passenger2)

print(train)
print(car1)
print(car2)
