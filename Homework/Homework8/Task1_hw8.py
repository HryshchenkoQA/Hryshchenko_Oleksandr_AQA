
'''
Реалізуйте біблиотеку з будь-яким функціоналом.
Наприклад, створіть функції для арифметичних операцій і побудуйте каскад імпортів з декількох packagів.
Має бути можливіcть імпортувати деякі функції з пакета, але не всі.
'''

from folder4task1 import is_master, age_group, choice

is_master(name="Alex")
#if __name__ == "__Task1_hw8__":
if __name__ == "__main__":
  name = input("Hi, what is your name? Enter here, please: ")
  greeting = is_master(name)
  print(greeting)


age_group(age='10')
#if __name__ == "__Task1_hw8__":
if __name__ == "__main__":
  age = input('Enter your age here: ')
  greeting = age_group(age)
  print(greeting)


choice(cinema="why")
#if __name__ == "__Task1_hw8__":
if __name__ == "__main__":
  cinema = input("Barbie or Oppenheimer? Or maybe both of them?): ")
  answer = choice(cinema)
  print(answer)