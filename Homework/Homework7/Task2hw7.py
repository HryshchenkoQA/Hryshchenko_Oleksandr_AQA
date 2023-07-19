'''
Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt) і повертає список усіх прізвищ з нього.
Кожен рядок файлу містить номер, прізвище, країну. Файл створити власноруч і записати туди дані
'''
import csv
with open("txt_for_HW7/names.csv", "w") as names:
    name_fields = ['number', 'name', 'surname' 'country']
    name_dict_write = csv.DictWriter(names, fieldnames=name_fields)
    names_dict_writer.writeheader()
    first_row.writerow({'number': 1, 'name': 'Alex', 'surname': 'Hryshchenko', 'country': 'Ukraine'})




# with open('birthday2.csv', 'w') as birthday:
#     birthday_fieldnames = ['name', 'group', 'birthday']
#     birthday_dict_writer = csv.DictWriter(birthday, fieldnames=birthday_fieldnames)
#     birthday_dict_writer.writeheader()
#     birthday_dict_writer.writerow({'name': 'Emanual', 'group' : 'french', 'birthday': 8})
#     birthday_dict_writer.writerow({'name': 'Boris', 'group': 'english', 'birthday': 10})

 # f.write("1, James, Bond, UK\n"
 #          "2, Jane, Smith, Canada\n"
 #          "3, Peter, Smith, United Turkey\n"
 #          "4, Alex, Hryshchenko, Ukraine")