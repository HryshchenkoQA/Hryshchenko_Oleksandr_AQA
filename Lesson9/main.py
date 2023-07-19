#import Lesson9.math_module as module
#from Lesson9 import *                       # '*' = all import
#from Lesson9 import math_module
# from Lesson9.folder1.folder2.folder3.math_module import summ as summ1        #можно перечислять функции через запятую
# from Lesson9.folder1.folder2.folder3.math_module2 import summ as summ2


first_person_salary = 70
second_person_salary = 120

#print(module.summ(first_person_salary, second_person_salary))
#print(summ)
#print(math_module.summ(first_person_salary, second_person_salary))

from Lesson9 import summ as summ1
from Lesson9.folder1.folder2.folder3.math_module2 import summ as summ2

print(summ1(first_person_salary,second_person_salary))
print(summ2(first_person_salary, second_person_salary, 500))
import Lesson9
print(Lesson9.summ(1,2))

from Lesson9.new_directory.new_directory1.aplication1 import summ as new_excellent_summ
print(new_excellent_summ(15,20))