import math
import random
first_value = 2                             #integer (целое число)
g_value = 9.8                       #float (плавающая запятая)
message = 'This is message'         #string (строка)
result = True                       #bool
empty_result = None                 #nontype

'''
print(one)
print(type(one))
print(id(one))
print(id(g_value))
print(id(empty_result))
'''
'''second_value = 4
third_value = first_value + second_value
print(third_value)

print(third_value - first_value)
print(first_value * second_value)
print(second_value / first_value)
print(second_value // first_value)
print(4 // 2)
print(2 % 4)
print(3**2)
print(3**3)
print(2 +3 * 4)
print((2+3) * 4)
small_number = 0.1 * 0.1
print(round(small_number, 2))
'''
'''
print(pi * R**2)
print(math.cos(2))
print(math.pi)
'''

'''
pi = math.pi
R = 2
random_number = random.randint(1,50)
print(random_number)
print(pi * random_number**2)
print(random.randrange(15))
print(random.choice(['god exist, 'you exist']))'''

print(dir('aaa'))
my_name = 'My name'
#print(my_name.title())
#print(my_name.upper())
#print(my_name.lower())

first_name = 'Bruece'
second_name = 'Wayne'
full_name = first_name + ' '+  second_name
print("Hello, " + full_name)
print('\tpython')
print('hello, my name is ' + full_name + '\nand \nim \nhere \nto \nlearn \npython')

first_string = 'Python'
second_string = 'python '
print(second_string.rstrip()) #удаление пробелов справа(right)
print((first_string.lstrip())) #удаление пробелов слева (left)

company_info = 'amazon is very huge company, unfortunately'
#print(company_info.capitalize()) #сделать первую букву большой
print(company_info.replace('Amazon', 'Apple'))
print('is' in company_info)
print(company_info.islower())
print(company_info.isupper())
print(company_info.isalpha())
print(first_name.isalpha())
print('  '.isspace())
print('4'.isdigit())
four_aplha = '4'
for_numeric = 4
print(company_info.count('a'))
print(company_info.index('m'))
print(company_info.find('5')) #безопасный поиск
print(len(company_info))
print(company_info.split('very'))
print('this is first line\nthis is second line'.splitlines())
print(company_info[21])
print(company_info[21:])
print(company_info[21:30])
print(company_info[:30])
print(company_info[21:30:2])

food = 'Solyanka'
price = 90
print('Food is {} and price is {}'.format(food, price))
print(f'food is {food}, price is {price}')
