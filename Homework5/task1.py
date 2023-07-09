'''
Напишіть програму на Python для знаходження перетину двох заданих масивів за допомогою лямбда.
'''
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

same_numbers = list(filter(lambda x: x in list1, list2))

print(same_numbers)
