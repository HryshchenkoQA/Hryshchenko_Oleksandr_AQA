'''
Создайте с помощью list comprehension список, в котором будет 100 элементов, и каждый из которых будет в границах
от 1 до 10(для этого можно воспользоваться функцией randint из модуля random).
Посчитайте количество каждого элемента и выведите в консоль
'''

import random

numbers = [random.randint(1, 10) for i in range(100)]

counts = {}
for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

for number, count in counts.items():
    print(number, count)

print(numbers)