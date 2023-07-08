'''
1.Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому,
так і другому списках, і надрукуйте їх у порядку зростання.
'''
def find_common_numbers(list1, list2):
    common_numbers = sorted(set(list1) & set(list2))
    for number in common_numbers:
        print(number)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
find_common_numbers(list1, list2)

