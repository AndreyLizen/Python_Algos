"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit
import cProfile

# 1) задача 4 урока 3
# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2]
my_list = [el for el in range(100, 1001) if el % 2 == 0]

def f1():
    max_repeat_el = max(my_list, key=my_list.count)
    print(my_list)
    print(f"Наибольшее число повторений в массиве у числа {max_repeat_el}, количество повторений: {my_list.count(max_repeat_el)}.")

def f2():
    max_repeat = 0
    for i in range(len(my_list)):
        if my_list.count(my_list[i]) > max_repeat:
            max_repeat = my_list.count(my_list[i])
            max_repeat_el = my_list[i]
    print(my_list)
    print(f"Наибольшее число повторений в массиве у числа {max_repeat_el}, количество повторений: {max_repeat}.")


# t1 = timeit.Timer("f1()", "from __main__ import f1")
# print("Функция с использованием max с ключом: ", t1.timeit(number=1000), "milliseconds")
# t2 = timeit.Timer("f2()", "from __main__ import f2")
# print("Функция с использованием цикла: ", t2.timeit(number=1000), "milliseconds")

# 1.1) Результаты при простом исходном списке:
# Функция с использованием max с ключом:  0.050876189 milliseconds
# Функция с использованием цикла:  0.041872239000000006 milliseconds
# Результаты были показаны одного порядка, при этом, при каждом запуске результат меняется
# от 0,3 до 0,8 миллисекунд для обеих функций. В целом, можно говорить об одинаковой скорости работы
# функций с использованием max с ключом и с использованием цикла for.

# 1.2) Результаты при большом исходном списке, получаемом по генератору (см. код выше):
# Функция с использованием max с ключом:  5.238644697 milliseconds
# Функция с использованием цикла:  4.7645249960000005 milliseconds
# Результаты были показаны одного порядка, при этом, при каждом запуске результат меняется
# примерно на +-10% для обеих функций. В целом, можно говорить о незначительном
# преимуществе в скорости работы функции с использованием цикла for.

# 1.3)
# cProfile.run('f1()')
# cProfile.run('f2()')
# # cProfile показывает:
# 8 function calls in 0.005 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.000    0.000    0.005    0.005 task_1.py:22(f1)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#         1    0.004    0.004    0.004    0.004 {built-in method builtins.max}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#  459 function calls in 0.009 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#         1    0.000    0.000    0.009    0.009 task_1.py:27(f2)
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       452    0.008    0.000    0.008    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile показывает преимущество по скорости функции с использованием max с ключом за счет меньшего
# количества обращений. Результат в целом разнонаправленный с timeit!!!


# 2) задача 3 урока 2
def cycle_decision(number):
    rev_number = 0
    while number != 0:
        rev_number = (rev_number * 10) + (number % 10)
        number = number // 10
    return rev_number

def recur_decision(number, rev_number=0):
    if number == 0:
        return rev_number
    else:
        rev_number = (rev_number * 10) + (number % 10)
        number = number // 10
        return recur_decision(number, rev_number)

# t1 = timeit.Timer("cycle_decision(1122334455)", "from __main__ import cycle_decision")
# print("Прямая функция: ", t1.timeit(number=1000000), "milliseconds")
# t2 = timeit.Timer("recur_decision(1122334455, rev_number=0)", "from __main__ import recur_decision")
# print("Функция с рекурсией: ", t2.timeit(number=1000000), "milliseconds")

# 2.1) Результаты сравнения прямой функции и функции с рекурсией (вычислений по 1 млн)
# Прямая функция:  2.5753793629999997 milliseconds
# Функция с рекурсией:  4.016369856 milliseconds
# Результаты были показаны одного порядка, при этом, при каждом запуске результат меняется
# примерно на +-10% для обеих функций. В целом, можно говорить о преимуществе
# в скорости работы прямой функции над рекурсивной на примерно 30%.

# 2.2)
cProfile.run('cycle_decision(11111111111111111111122334455)')
cProfile.run('recur_decision(11111111111111111111122334455, rev_number=0)')
# Результаты (таблицы по нулям):
# # Прямая функция: 4 function calls in 0.000 seconds
# # Функция с рекурсией: 33 function calls (4 primitive calls) in 0.000 seconds
# Как показывает предыдущая оценка cProfile, функуия с меньшим количеством
# вызовов эмпирически имеет преимущество по скорости. Установить степень преимущества в данном случае невозможно.

# 3). Проанализировать сложность одного любого алгоритма
# def cycle_decision(number):
#     rev_number = 0
#     while number != 0:
#         rev_number = (rev_number * 10) + (number % 10)
#         number = number // 10
#     return rev_number
# Сложность линейная O(n)