'''
Напишіть програму на Python, щоб знайти список із максимальною та мінімальною довжиною за допомогою лямбда.
'''
string1 = ['apple', 'banana']
string2 = ['Volvo', 'Hyundai', 'Honda', 'Kia']
string3 = ['Nokia', 'samsung', 'htc', 'xiaomi', 'LG', 'Huawei']

all_strings = [string1, string2, string3]

string_finder = list(map(lambda x: len(x), all_strings))
max_length = max(string_finder)
min_length = min(string_finder)

strings_with_max_length = list(filter(lambda x: len(x) == max_length, all_strings))
strings_with_min_length = list(filter(lambda x: len(x) == min_length, all_strings))

print("Список з максимальною довжиною:", strings_with_max_length)
print("Список з мінімальною довжиною:", strings_with_min_length)