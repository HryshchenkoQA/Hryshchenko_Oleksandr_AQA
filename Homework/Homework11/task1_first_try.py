'''
Опишите объекты искусства для музея. воспользуйтесь всеми 5 принципами: абстракция, наследование, полиморфизм, скрытие,
инкапсуляция. добавьте property, setter. Создайте хотя-бы по одному инстансу каждого класса и вызовите методы
'''
class ArtObject:
    def __init__(self, name, age, author):
        self.name = name
        self.age = age
        self.author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Author: {self.author}"


class Painting(ArtObject):
    def __init__(self, name, age, author, height, weight):
        super().__init__(name, age, author)
        self.height = height
        self.weight = weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    def __str__(self):
        return f"{super().__str__()}, Height: {self.height}, Weight: {self.weight}"


class Sculpture(ArtObject):
    def __init__(self, name, age, author, material):
        super().__init__(name, age, author)
        self.material = material

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value

    def __str__(self):
        return f"{super().__str__()}, Material: {self.material}"


painting1 = Painting("Mona Lisa", 500, "Leonardo da Vinci", 21, 7)
painting2 = Painting("The Starry Night", 1889, "Vincent van Gogh", 29, 36)

sculpture1 = Sculpture("The Thinker", 1904, "Auguste Rodin", "bronze")
sculpture2 = Sculpture("David", 1501, "Michelangelo", "marble")

print(painting1)
print(painting2)
print(sculpture1)
print(sculpture2)