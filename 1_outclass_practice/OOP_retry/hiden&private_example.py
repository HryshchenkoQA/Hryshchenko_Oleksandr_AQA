from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, salary, position):
        self.salary = salary
        self.position = position
    @abstractmethod
    def do_work(self):
        pass

class Engineer(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)


    def do_work(self):
        print("Im working")

    def _create_new_freamwork(self):
        print('freamwork in progress')

class Programmer(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print("Im writing programms")

engineer = Engineer(2100, "junior")

# engineer.do_work()
# engineer.position()
# engineer.salary()
engineer._create_new_freamwork