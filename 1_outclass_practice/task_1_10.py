'''
Напишите функцию max_of_three, которая принимает три числа в качестве аргументов и возвращает наибольшее из них.
'''
def max_of_three(first, second, third):
    max_num =first
    if second > max_num:
        max_num = second
    if third > max_num:
        max_num = third
    return max_num
result = max_of_three(110,40,50)
print(result)