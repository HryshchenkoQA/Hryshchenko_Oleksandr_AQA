# some_list = [1,2,3,4,5]
# new_list = []
# for item in some_list:
#     if item >3:
#         new_list.append(item)
# print(new_list)
#
# new_list_comprehension = [item for item in some_list if item > 3]
# print(new_list_comprehension)


# new_list = [item ** 2 for item in range(1000)]
# print(new_list)
#
# names = ['Jhoan', 'Jennifer', 'Jeka']
# new_dict = {index: name for index, name in enumerate(names)}
# enumerated_list =enumerate(names)
# for element in enumerated_list:
#     print(element)
# print(enumerated_list)
# print(new_dict)

# doubled_list =[1,2,2,4,6,9,16,7,8,10]
# new_set = {item for item in doubled_list if item>4}
# print(new_set)
# new_set =set(doubled_list)
# print(new_set)

new_gen = (item for item in range(1000))
# for item in new_gen:
#     print(item)
print(new_gen)
new_tuple = (*(item for item in range(1000)),)
print(new_tuple)
