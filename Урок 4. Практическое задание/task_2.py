"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit

def naive_method(i):
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

def sieve_method(i):
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [el for el in sieve if el != 0][i-1]

i = int(input('Введите порядковый номер простого числа: '))
print(naive_method(i))
print(sieve_method(i))

# print(timeit.timeit("naive_method(i)"), setup="from __main__ import naive_method, i", number=100)
# print(timeit.timeit("eratosfens_sieve_method(i)"), setup="from __main__ import eratosfens_sieve_method, i", number=100)
t1 = timeit.Timer("naive_method(1000)", "from __main__ import naive_method")
print("Наивная функция: ", t1.timeit(number=100), "milliseconds")
t2 = timeit.Timer("sieve_method(1000)", "from __main__ import sieve_method")
print("Функция с использованием решета Эратосфена: ", t2.timeit(number=100), "milliseconds")

# Результаты вычислений:
# 1) При i = 10:
# Наивная функция:  0.003192426000000026 milliseconds
# Функция с использованием решета Эратосфена:  0.5410727700000004 milliseconds

# 2) При i = 100:
# Наивная функция:  0.31102133799999976 milliseconds
# Функция с использованием решета Эратосфена:  0.5115749650000003 milliseconds

# 2) При i = 100:
# Наивная функция:  53.934670368 milliseconds
# Функция с использованием решета Эратосфена:  0.5175402670000011 milliseconds

# По результатам можно говорить о том, что функция с использование решета Эратосфена имеет
# постоянную O(1) сложность, а наивный метод - сложность квадратичную O(n**2)