'''
Напишите адаптер, который конвертирует json в csv. т.е. делает обратную конвертацию от той, что
мы реализовали на уроке. Пример из урока, а также json и csv добавлено, формат записи данных тот же.
'''
"""
import json
import csv

class CsvConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as csv_file:
            lines = csv.DictReader(csv_file)
            for line in lines:
                self.__lines.append(line)
        print(self.__lines)

class JsonConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            lines = json.load(json_file)
            for line in lines:
                self.__lines.append(line)
        print(self.__lines)


converter1 = CsvConverter()
converter2 = JsonConverter()
converter1.read_file("example.csv")
converter2.read_file("example.json")
"""

import csv
import json

class CsvConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as csv_file:
            lines = csv.DictReader(csv_file)
            for line in lines:
                self.__lines.append(line)
        print(self.__lines)

    def write_file(self, filename: str):
        with open(filename, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.__lines[0].keys())
            writer.writeheader()
            for line in self.__lines:
                writer.writerow(line)


class JsonConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            lines = json.load(json_file)
            for line in lines:
                self.__lines.append(line)
        print(self.__lines)

    def write_file(self, filename: str):
        with open(filename, 'w') as json_file:
            json.dump(self.__lines, json_file)


converter1 = CsvConverter()
converter2 = JsonConverter()
converter1.read_file("example.csv")
converter1.write_file("example_out.csv")
converter2.read_file("example.json")
converter2.write_file("example_out.json")






