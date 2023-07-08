'''
3.Створіть списки із значеннями для name, surname, location, наприклад name = ['Alex', 'John', 'Simba'].
напишіть програму, яка створює словники з даними випадкових людей на основі ваших списків, роздрукуйте результат.
для випадковості значень скористайтесь модулем random. приклад згенерованого словника:

{'name':'Liza', 'surname':'Djoconda', 'location':'Florence'}
'''
# import random
# name = ["Alex", "Petya", "Vasya", "Katya", "Masha", "Olya", "Julia"]
# surname = ['Wick', 'Williams', 'Black', 'Moore', "Cola", "Pentyuk", "Roberst"]
# location = ['USA', 'Canada', 'Ukraine', 'Poland', 'Moldova', 'England', 'Scotland']
# random_data = {'name': random.choice(name), 'surname': random.choice(surname), "location": random.choice(location)}
# print(random_data)

import random

def generate_random_person(name, surname, location):
    person = {
        'name': random.choice(name),
        'surname': random.choice(surname),
        'location': random.choice(location)
    }
    return person

name = ["Alex", "Petya", "Vasya", "Katya", "Masha", "Olya", "Julia"]
surname = ['Wick', 'Williams', 'Black', 'Moore', "Cola", "Pentyuk", "Roberst"]
location = ['USA', 'Canada', 'Ukraine', 'Poland', 'Moldova', 'England', 'Scotland']

random_person = generate_random_person(name, surname, location)
print(random_person)
