class Donkey:
    strenght = 10
    @classmethod
    def print_strenght(cls):
        print(cls, cls.strenght)

class Horse:
    speed = 20
    strenght = 15

    @classmethod
    def print_strenght(cls):
        print(cls, cls.strenght)

class Mul(Donkey, Horse):
    pass

mul1 = Mul()
print(mul1.strenght)
print(mul1.speed)
mul1.print_strenght()

class Human:
    def m(self):
        print("A")

class Child1(Human):
    def m(self):
        print("B")

class Child2(Human):
    def m(self):
        print("C")
class GrandChild(Child1,Child2):
   # pass
    def m(self):
        print("D")

    def m_from_second_parent(self):
        Child2.m(self)



grandChild = GrandChild()
grandChild.m()
grandChild.m_from_second_parent()