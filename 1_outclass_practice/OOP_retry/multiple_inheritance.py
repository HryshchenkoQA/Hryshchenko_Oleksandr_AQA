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
print(mul1.print_strenght())



# class_tests Human:
#     def m(self):
#         print('A')
#
# class_tests Child1(Human):
#     def m(self):
#         print('B')
#
# class_tests Child2(Human):
#     def m(self):
#         print('C')
#
# class_tests GrandChild(Child1, Child2):
#     def m(self):
#         print('D')
#
#     def m_from_second_parent(self):
#         Child2.m(self)
#
# grandchild=GrandChild()
# grandchild.m()
# grandchild.m_from_second_parent()