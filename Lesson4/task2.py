import random
list_of_numbers = [5,8,3,4,8,1,3,7,4,3]
value = 0
while True:
    value_temporary = input('print:')
    if value_temporary == 'summ':
        break
    elif value_temporary.isnumeric():
        value += int(value_temporary)
        print(value)
    else:
        print('you input wrong word')
        continue
print(value)
