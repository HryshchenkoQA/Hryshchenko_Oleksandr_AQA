'''
Задача 2. В змінній birth_month запишіть номер місяця вашого народження (дані введіть з консолі). В залежності від
введених даних виведіть характеристику для відповідної пори року:

Зима - За вікном падав сніг.

Весна - Все довкола розцвітало.

Літо - Діти насолоджувались літніми канікулами.

Осінь - Все довкола загоралось яскравими фарбами.
'''

date_birth = int(input("Введіть номер місяця вашого народження:"))
if date_birth == 12 or date_birth == 1 or date_birth == 2:
    print("Зима - За вікном падав сніг")
elif date_birth == 3 or date_birth == 4 or date_birth == 5:
    print("Весна - Все довкола розцвітало")
elif date_birth == 6 or date_birth == 7 or date_birth == 8:
    print("Літо - Діти насолоджувались літніми канікулами.")
elif date_birth == 9 or date_birth == 10 or date_birth == 11:
    print("Осінь - Все довкола загоралось яскравими фарбами")
else:
    print("Введений некоректний номер місяця")