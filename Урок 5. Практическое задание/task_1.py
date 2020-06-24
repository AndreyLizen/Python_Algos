"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p)
Point(x=1, y=2)
print(p.x)
print(p[0])

n = int(input('Введите количество предприятий для расчета прибыли: '))

def new_firm():
    summa = 0
    firm = namedtuple(input("Введите наименование предприятия: "), summa)
    my_list = input("Введите сумму прибыли для предприятия поквартально через пробелы (4 числа), затем 'Enter': ").split()
    for el in my_list:
        if not el.isdigit():
            summa = 0
            my_list = []
            print("Вы ввели нечисловой символ! Перезапустите программу и попробуйте всё заново.")
            break
        summa = summa + int(el)

    return firm

firms = []
total_sum = 0
for i in range(n):
    firms.append(new_firm())
    print(new_firm())

# Я просто в дикой ярости!!!
# ПОЧЕМУ нельзя передать в именованный кортеж имя со стороны, а нужно его явно указывать?
# Да, я пробовал всё и по разному - не передается, выдает ошибки!!!
# Почему об этом ничего не было сказано на уроке?
# Мне легко сделать нужный код БЕЗ этой бесполезной штуки - namedturple, просто очень неприятно
# самому откапывать неработоспособность коллекций