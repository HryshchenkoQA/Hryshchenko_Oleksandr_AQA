from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, salary, position):
        self.salary = salary
        self.position = position
    @abstractmethod
    def do_work(self):
        pass
    def do_another_work(self):
        print(2+5)




class Toyota_employee(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('Im doing Toyota stuff')

class Renault_employee(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('Im doing Renault stuff')



worker1 = Toyota_employee('worker1', 2100)
