'''
a = input("write here integer")
integer_value_a = int(a)
print(a)

a = input()
print(a)
'''

# булевые значение (true/false)
'''
this_is_true = True
this_is_true_integer = int(this_is_true)
print(this_is_true_integer)
this_is_empty_string = ''
print(bool(this_is_empty_string))
'''

# < less
# >more
# <= less or equal
# >= more or equal
# == equal
# != not qual

'''
a = input("please insert a")
a_int = int(a)
if a_int > 5:
    print("congratilations")
elif a_int < 3:
    print("try harder")
else:
    print("sorry you not a winner")
    '''
'''
#or
first_value = 20
if type(first_value) == int or first_value < 25:
    print("its above 20")
    


#and
second_value = 15
if second_value <= 16 and second_value > 10:
    print("its above 13")

print(bool(0))
print(bool(0.01))

#not
third_value = 5
if third_value >4 and not second_value > 20:
    print("a")
'''

'''
eyes = int(input("number of eyes"))
legs = int(input("number of legs"))
if eyes == 8:
    if legs == 8:
        print("this is spider")
    elif legs == 6:
        print("this is fly")
    else:
        print("undefiened")
elif eyes == 1:
    print("this is cyclope or God Odin")
elif eyes > 1 and eyes < 8:
    print("beyond your compr..")
'''
'''
our_first_list = [2,5,3,5,8, "text", 9.0]
our_second_list = []
our_third_list = list()
print(len(our_first_list))
print(our_first_list[5])
print(our_first_list.index(5))
our_first_list.append(8)
print(our_first_list)
our_first_list.insert(3,11)
print(our_first_list)
our_first_list.remove(5)
print(our_first_list)
our_first_list.pop()
print(our_first_list)
our_first_list.pop(0)
print(our_first_list)
del our_first_list[1]
print(our_first_list)
our_first_list.clear()
print(our_first_list)
'''

'''
another_list = [9, 3, 6, 2, 6, 9, 5, 1]
another_list.sort(reverse=False)
print(another_list)
another_list = [9, 3, 6, 2, 6, 9, 5, 1]
simple_list = [1, 2, 3]
another_list.sort(reverse=True)
print(another_list)
print(another_list[:5])
print(another_list[1:])

another_list.extend(simple_list)
print(another_list)

simple_list.extend(another_list)
another_list = simple_list
print(another_list)
'''
