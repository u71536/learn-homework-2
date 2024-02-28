"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору.
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

# -*- coding: utf-8 -*-
import csv

dictionary = [
    {"name": "Раф", "age": "123", "job": "manager", "city": "Moscow"},
    {"name": "Димитрий", "age": "87", "job": "janitor", "city": "London"},
    {"name": "Виктор", "age": "43", "job": "accountant", "city": "Paris"},
    {"name": "Оскар", "age": "15", "job": "developer", "city": "Riga"}
]

def main():
    with open('export.csv', 'w', encoding='utf-8', newline='') as newfile:
        fields = ['name', 'age', 'job', 'city']
        writer = csv.DictWriter(newfile, fields, delimiter=";")
        writer.writeheader()
        for row in dictionary:
            writer.writerow(row)


if __name__ == "__main__":
    main()
