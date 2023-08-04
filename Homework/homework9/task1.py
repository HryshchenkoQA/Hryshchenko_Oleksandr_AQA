'''
Создайте класс с описанием любого животного. Добавьте 1 static method, 3 обычных метода
'''
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    @staticmethod
    def get_all_dogs():
        return [Dog(name, breed, age) for name, breed, age in dogs]

    def bark(self):
        """Лает."""
        print(f"{self.name} лает!")

    def fetch(self):
        print(f"{self.name} ищет и приносит палку!")

    def roll_over(self):
        print(f"{self.name} перекатывается через спину!")


dogs = [
    ("Max", "Golden Retriever", 5),
    ("Bella", "Labrador Retriever", 3),
    ("Charlie", "Pug", 2),
]

if __name__ == "__main__":
    dogs = Dog.get_all_dogs()
    for dog in dogs:
        print(dog.name)
    dogs[0].bark()
    dogs[1].fetch()
    dogs[2].roll_over()
