'''
Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt) і повертає список усіх прізвищ з нього.
Кожен рядок файлу містить номер, прізвище, країну. Файл створити власноруч і записати туди дані
'''

import csv

with open('txt_for_HW7/names.txt', 'w') as names:
    names_fields = ['Number', 'Name', 'Surname', 'Country']
    names_dict_writer = csv.DictWriter(names, fieldnames= names_fields, delimiter = ',')
    names_dict_writer.writeheader()
    names_dict_writer.writerow({'Number': '1', 'Name': 'James', 'Surname': 'Bond', 'Country': 'UK'})
    names_dict_writer.writerow({'Number': '2', 'Name': 'Jane', 'Surname': 'Smith', 'Country': 'Canada'})
    names_dict_writer.writerow({'Number': '3', 'Name': 'Peter', 'Surname': 'Green', 'Country': 'Turkey'})
    names_dict_writer.writerow({'Number': '4', 'Name': 'Alex', 'Surname': 'Hryshchenko', 'Country': 'Ukraine'})


def get_surnames():
    with open('txt_for_HW7/names.txt', 'r') as names:
        names_reader = csv.DictReader(names, delimiter=',')
        surnames = []
        for row in names_reader:
            surnames.append(row['Surname'])
    return surnames

surnames = get_surnames()
print(surnames)



