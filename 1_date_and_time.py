"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime


def print_days():
    date_today = datetime.datetime.now()
    date_yesterday = date_today - datetime.timedelta(days=1)
    date_month_ago = date_today - datetime.timedelta(days=30)
    print(f'Вчера было: {date_yesterday}')
    print(f'Сегодня: {date_today}')
    print(f'30 дней назад: {date_month_ago}')


def str_2_datetime(date_string):
    date_dt = datetime.datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return date_dt


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
