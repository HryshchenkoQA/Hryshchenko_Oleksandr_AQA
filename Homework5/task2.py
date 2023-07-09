'''
Напишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда
'''

list1 = ["123", "3.14", "-10", "abc", "2+2", "123aa"]
number = lambda x: x.replace('.', '', 1).isdigit()

for x in list1:
    if number(x):
        print(f"{x} є числом")
    else:
        # print(f"{x} не є числом")
        break