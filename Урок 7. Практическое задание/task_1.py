"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from random import randint
from timeit import timeit

def bubble_decrease(my_list):
    n = 1
    while n < len(my_list):
        for i in range(len(my_list)-n):
            if my_list[i] < my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        n += 1
    return my_list

def bubble_decrease_upgraded(my_list):
    n = 1
    k = 0
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                k = 1
        if k == 0:
            break
        n +=1
    return my_list


my_list = [randint(-100, 100) for i in range(10)]
print(bubble_decrease(my_list))
print(bubble_decrease_upgraded(my_list))

print(timeit("bubble_decrease(my_list)", setup="from __main__ import bubble_decrease, my_list"))
print(timeit("bubble_decrease_upgraded(my_list)", setup="from __main__ import bubble_decrease_upgraded, my_list"))

# Результат отработки:
# [97, 70, 22, -5, -53, -60, -65, -72, -72, -84]
# [97, 70, 22, -5, -53, -60, -65, -72, -72, -84]
# Простой метод по убыванию: 13.141634825999999
# Усовершенствованный метод: 2.0607669289999997
# Усовершенствованный метод существенно увеличивает скорость сортировки
