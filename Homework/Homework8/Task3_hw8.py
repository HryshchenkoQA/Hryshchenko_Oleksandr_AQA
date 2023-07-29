'''
Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів.
Приймає на вхід будь-яку дату та час (datetime), а також значення днів(int), і знак
(True або False, які репрезентують + і -).
Повертає datetime. В цій задачі скористайтесь datetime.timedelta
'''

import re
import datetime

def add_days(date, days, sign):
  try:
    if sign:
      new_date = date + datetime.timedelta(days=days)
    else:
      new_date = date - datetime.timedelta(days=days)
  except ValueError:
    print("Date error")
    exit()

  return new_date

if __name__ == "__main__":
  date = input("Enter date in format YYYY-MM-DD: ")
  days = int(input("Enter days number: "))
  sign = input("Enter a sign: + or - ")

  new_date = add_days(datetime.datetime.strptime(date, "%Y-%m-%d"), days, sign)

  print(f"New date: {new_date}")
