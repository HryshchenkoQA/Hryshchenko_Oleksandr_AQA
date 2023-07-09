'''
Напишіть програму, в яку спочатку запишіть в 1 змінну ваше ім'я, в 2 ваше прізвище,
а потім виводить на екран повідомлення з вашими особистими даними.
Тут використайте конкатенацію, тобто об'єднайте стрічки.
'''
first_name = '   oleksandr   '
last_name = '   hryshchenko    '
full_name = first_name + ' ' + last_name
capitalized_name = full_name.title()
welcome_message = 'welcome back, dear' + ' ' + capitalized_name + ' ' + 'glad to see you again:)'
print(welcome_message)

'''
Виведіть результат в нижньому, верхнього регістрах з капіталізацією перших букв кожного слова.
'''
print(welcome_message.upper())
print(welcome_message.lower())
print(welcome_message.title())

'''
Змініть значення своєї змінної, яку ви створили на кроці 1 , додавши до свого імені декілька пробілів на початку та вкінці.
Прослідкуйте щоб \t \n зустрічались хоча б один раз. Виведіть нове значення. Видаліть пропуски і збережіть новий результат.
'''
modified_full_name = first_name.lstrip().rstrip() + ' ' + last_name.lstrip().rstrip()
welcome_message = '\twelcome back, dear' + ' ' + modified_full_name + ' ' + '\nglad to see you again:)'
welcome_message1 =welcome_message.capitalize()
print(welcome_message1)