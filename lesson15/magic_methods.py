class Horse:
    def __init__(self):
        self.speed = 5
        self.age = 4

    def __add__(self, other):
        return Mul(other.strenght, self.speed)


class Donkey:
    def __init__(self):
        self.strenght = 10
        self.age = 5

class Mul:
    def __init__(self, strenght, speed):
        self.strenght = strenght
        self.speed = speed

    def __str__(self):
        return f"{self.__class__.__name__}\nspeed: {self.speed}\nstrenght: {self.strenght}"

horse = Horse()
donkey = Donkey()
mul = horse + donkey
print(mul)

