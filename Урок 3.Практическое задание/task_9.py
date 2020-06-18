"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
from random import randint

def matrix_filling(rows, columns):
    global matrix
    matrix = []
    for row in range(rows):
        matrix.append([])
        for column in range(columns):
            matrix[row].append(randint(0, 100))


rows = int(input(f'Введите количество строк матрицы: '))
columns = int(input(f'Введите количество столбцов матрицы: '))
matrix_filling(rows, columns)
for i in range(len(matrix)):
    print(matrix[i])

print("Минимальные элементы каждого из столбцов матрицы:")
min_column_els = []
for i in range(columns):
    min_list = []
    for j in range(rows):
        min_list.append(matrix[j][i])
    min_column_els.append(min(min_list))
print(min_column_els)

print(f"максимальный элемент среди минимальных элементов стоблцов матрицы: {max(min_column_els)}")