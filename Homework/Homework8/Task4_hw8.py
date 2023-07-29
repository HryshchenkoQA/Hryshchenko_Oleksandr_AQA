'''
Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні),
вираховуючі різницю між наданим значеням і значенням datetime.now().
Приймає дату та час(datetime), повертає два значення: datetime і datetime.timestamp. В цій задачі скористайтесь
для конвертації datetime.timestamp. Виведіть результат в консоль
'''
import datetime

#birthday = input("Enter your date of birthday (YYYY-MM-DD HH:MM;SS): ")

birthday = datetime.datetime(year=1999,month=9,day= 9,hour=9,minute=9,second=9)
time_now = datetime.datetime.now()
age = (time_now-birthday).days // 365
age2= time_now.timestamp() - datetime.datetime.timestamp(birthday)

print(f"You are {age} years old.\nAnd your timestamp age is {age2}")
