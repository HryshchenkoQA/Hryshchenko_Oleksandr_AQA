class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Employee(Human):
    def __init__(self, name, age, gender, salary, position):
        super().__init__(name, age, gender)
        self.salary = salary
        self.position = position

worker1 = Employee('Andy', 30, 'male', 300, "QA")
