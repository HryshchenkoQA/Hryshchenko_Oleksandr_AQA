class Person():
    '''инициализируем атрибуты человека'''

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        '''получение описания человека'''
        description = self.name + " " + str(self.age) + " " + str(self.height) + " " + str(self.weight)
        print(description)

    def get_weight(self):
        print("weight of our human: " + str(self.weight))

    def update_weight(self, kg):
        self.weight = kg


class Warrior(Person):
    '''Create warrior class'''

    def __init__(self, name, age, height):
        ''' инициализируем атрибуты родительского класса (Персон)'''
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        print("Rage of our warrior: " + str(self.rage))

    def description_person(self):
        '''Переопределение родительского метода'''
        description = self.name + " " + str(self.age) + "her rage:  " + str(self.rage)
        print(description)


warrior = Warrior("Conon", 32, 200)
# warrior.update_weight(150)
warrior.description_person()
# # warrior.get_rage()
# #
# # man = Person("Alex", 27, 171)
# # # man.update_weight(140)
# # man.description_person()
# # # man.get_weight()

