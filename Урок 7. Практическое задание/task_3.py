"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

from timeit import timeit
from random import randint
from statistics import median

def median_1 (my_list):
    temp_list = my_list
    for i in range(len(my_list) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)

my_list = [randint(0, 100) for i in range(2 * randint(1, 10000) + 1)]

print(f'Исходный список:\n{my_list}\n')
print(f'Медиана, найденная через встроенную функцию - {median(my_list)}')
print(f'Медиана, найденная через функцию пользователя - {median_1(my_list)}')

print(f'Встроенная (median) {timeit("median(my_list)", globals=globals(), number=1000)} milliseconds')
print(f'Не встроенная (median_1) {timeit("median_1(my_list)", globals=globals(), number=1000)} milliseconds')

# Результаты теста скорости:
# Встроенная (median) 0.08691837399999999 milliseconds
# Не встроенная (median_1) 0.01034131499999999 milliseconds
# При любых вводных  данных не встроенная функция опережает по скорости функцию median модуля statistics!
# Интересно, почему?