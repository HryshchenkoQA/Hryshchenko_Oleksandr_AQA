def function_example(parametr1, parametr2 = 'im default parametr'):
    print(f'Hello! {parametr1}')
    print(f'and meet the {parametr2}')

function_example('first', parametr2= 'a')
function_example('second', 'b')
function_example('third')

def summ_of_two_numbers(first,second):
    result = first + second
    return result

a = summ_of_two_numbers(5,10)
b = summ_of_two_numbers(10,20)
c = summ_of_two_numbers(a,b)
print(c)

def summ_and_miltiply(first,second):     #arg
    result_of_summ = summ_of_two_numbers(first, second)   #first + second
    result_of_miltiply = first * second
    return result_of_summ, result_of_miltiply
first_result,second_result = summ_and_miltiply(5,20)
print(first_result)
print(second_result)
'''
def multiply_parametrs(*parametrs):
    for element in parametrs:
        print(element)

multiply_parametrs('papperoni')
multiply_parametrs('papperoni', 'carbonara', '4cheese')

def multiply_named_parametrs(**user_info):    # **kwargs
    for key, value in user_info.items():
        print(f'{key}: {value}')

multiply_named_parametrs(first_name = 'alejandro', second_name = 'formoza')


'''
