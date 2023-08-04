from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, salary, position):
        self.salary = salary
        self.position = position
    @abstractmethod
    def do_work(self):
        pass
        #raise NotImplementedError('Not implemented error')
# class Toyota_employee(Employee):
#     def __init__(self,salary, position):
#         super().__init__(salary, position)

    def do_work(self):
        print("Im doing Toyota stuff")
class Renault_emoloyee(Employee):
    def __init__(self,salary, position):
        super().__init__(salary, position)

    print("Im doing Renault stuff")

empoyee =Employee('worker',2000)
toyota_employee = Toyota_employee('worker', 2100)
