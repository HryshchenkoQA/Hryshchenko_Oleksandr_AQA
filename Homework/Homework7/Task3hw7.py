'''
Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) і повертає список словників
виду {"date": date} у яких date - це дата з рядка (якщо є),
Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
'''

import re

def dates_finder():
  with open('txt_for_HW7/authors.txt', "r") as f:
    dates = []
    for line in f:
      date = re.match(r"\d{1,2}(st|nd|rd|th) (January|February|March|April|May|June|July|August|September|October|November|December) \d{4}", line)
      if date:
        dates.append({"date": date.group()})

  for date in dates:
    print(date)

dates_finder()
