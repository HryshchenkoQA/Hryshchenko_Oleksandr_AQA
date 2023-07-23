'''
Створіть обробку одного будь-якого exception, який не використався як приклад на занятті. Виведіть результат в консоль
'''
name1 = input('Enter Here YOUR !NAME!: ')
try:
    name1 = int(name1)
except ValueError:
    print('its a exception prank (: ')
else:
    print("Hi, {}! but it's not your name, try again :D" .format(name1))




