class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class employee(Human):
    def __init__(self, name, age, gender, salary, position):
        super().__init__(name, age, gender)
        self.salary = salary
        self.position = position

goose = employee("Andy", 2, "male", "2 glass of watter", "good boy")
print(goose)

