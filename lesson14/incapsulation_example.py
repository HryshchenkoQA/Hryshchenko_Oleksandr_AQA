class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name


#полиморфизм

class Cat:
    def make_noise(self):
        pass


class Lion(Cat):
    def __init__(self):
        self.color = "yellow"
        self.age = 12
        self.speed = 60
        self.character = "Pride"

    def make_noise(self):
        print('Roaaaar!')

class Cheetah(Cat):
    def __init__(self):
        self.color = "Black"
        self.age = 10
        self.speed = 120
        self.character = "friendly"

    def make_noise(self):
        print('Meeow!')

king = Lion()
sweet_cheetah = Cheetah()
king.make_noise()
sweet_cheetah.make_noise()