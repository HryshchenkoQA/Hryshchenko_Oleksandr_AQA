import random
int1 = int(input("Потяните карту"))
int2 = random.randint(2, 14)
if int1 == 1:
    print("вы потянули карту")
    if int2 > 13:
        print("Туз")
    elif int2 > 12:
        print("король")
    elif int2 > 11:
        print("дама")
    elif int2 > 10:
        print("валет")
    else:
        print("10 or less")
elif int1 == 0:
    print("у вас все хорошо, не играйте в это")