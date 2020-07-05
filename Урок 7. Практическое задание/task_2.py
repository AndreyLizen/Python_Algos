"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import random

def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i = i + 1
            else:
                my_list[k] = right_half[j]
                j = j + 1
            k = k + 1
        while i < len(left_half):
            my_list[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            my_list[k] = right_half[j]
            j = j + 1
            k = k + 1


n = int(input("Введите количество элементов массива: "))
my_list = [random() * 50 for i in range(n)]

print(f"Исходный массив:\n{my_list}")
merge_sort(my_list)
print(f"Отсортированный массив:\n{my_list}")