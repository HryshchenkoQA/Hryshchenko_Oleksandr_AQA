'''
class Human:
    name = 'Andy'
    age = 30
    adress = []

andy:Human = Human()
samanhta:Human=Human()
print(andy)
print(samanhta)
print(andy.name)
print(samanhta.name)
samanhta.adress.append("1 Avenue")
andy.adress.append("2 Avenue")
print(andy.adress)
print(samanhta.adress)
'''

class Human:
    def __init__(self,name, age, adress = '1street', hair_color = 'Black'):
        self.name = name
        self.age = age
        self.adress = adress
        self.hair_color = hair_color
    def get_name(self):
        return self.name

    @classmethod
    def from_age_and_name(cls,name,age):
        return cls(name,age, '2street', 'white')

@staticmethod
def get_me_something():
    print("hello")


franky = Human.from_age_and_name('franky', 5,)
andy = Human('Andy', 30, '1street', 'black')
samantha = Human('Samantha',20, None, None)
print(samantha.get_name())
print(franky.hair_color)
samantha.get_me_something