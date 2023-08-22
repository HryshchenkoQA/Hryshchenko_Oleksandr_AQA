'''
Напишите адаптер, который конвертирует json в csv. т.е. делает обратную конвертацию от той, что
мы реализовали на уроке. Пример из урока, а также json и csv добавлено, формат записи данных тот же.
'''
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






