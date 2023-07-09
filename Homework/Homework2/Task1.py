'''
Задача 1. В змінній minute лежит число от 0 до 59, згенероване випадковим чином.
Визначте в якій четверті години попадає це число (в першій, другій, третій чи четвертій).
'''
import random
minute = int(input("Sign up 1 or 2"))
random_minute = random.randint(0, 59)
if minute == 1:
    print("Lets go")
    if random_minute < 15:
        print("your number in 1/4")
    elif random_minute < 30:
        print("your number in 2/4")
    elif random_minute < 40:
        print("your number in 3/4")
    elif random_minute < 59:
        print("your number in 4/4")
if minute == 2:
        print("Ok, see you soon")

'''
#or
import random
minute = random.randint(0, 59)
if minute < 15:
    quarter = "перша"
elif minute < 30:
    quarter = "друга"
elif minute < 45:
    quarter = "третя"
else:
    quarter = "четверта"
print("Число {} попадає в {} четверть години.".format(minute, quarter))
'''