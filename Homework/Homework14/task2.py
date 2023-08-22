'''
воспользуйтесь pytest. напишите функцию, которая добавляет в csv одну строку.
Напишите функцию, которая удаляет из csv одну строку. напишите два теста, которые проверяют соответственно
добавилась ли строка и удалилась ли она. в качестве проверочного csv можете воспользоваться
добавленным к заданию файлом или любым другим.
'''
import csv
import pytest

def add_row_to_csv(file_path, row):
  with open(file_path, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(row)

def remove_row_from_csv(file_path, row_number):
  with open(file_path, 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

  rows.remove(rows[row_number])

  with open(file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)


def test_add_row_to_csv(capsys):
  with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['a', 'b', 'c'])

  add_row_to_csv('test.csv', ['d', 'e', 'f'])

  with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

  assert rows == [['a', 'b', 'c'], ['d', 'e', 'f']]

  captured = capsys.readouterr()
  assert captured.out == ''


def test_remove_row_from_csv(capsys):
  with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['a', 'b', 'c'])
    writer.writerow(['d', 'e', 'f'])

  remove_row_from_csv('test.csv', 1)


  with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

  assert rows == [['a', 'b', 'c']]

  captured = capsys.readouterr()
  assert captured.out == ''
