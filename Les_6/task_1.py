"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или
несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
"""
# Python 3.10.2
# Windows 11 x64

from memory_profiler import memory_usage
from random import randint
from numpy import array


def memory_info(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# Не оптимизированная
@memory_info
def find_min():
    lst = [randint(1, 99) for _ in range(100000)]
    min_dig = lst[0]
    for i in lst:
        if min_dig > i:
            min_dig = i
    return min_dig


res, mem_diff = find_min()
print(mem_diff)


# Оптимизированная
@memory_info
def find_min_2():
    numpy_arr = array([randint(1, 99) for _ in range(100000)])
    yield min(numpy_arr)


res, mem_diff = find_min_2()
print(mem_diff)

"""
Сделал оптимизацию хранения элементов через numpy, использовал встроенные функции,
но максимальный эффект дал генератор

Результаты: 1 - 0.9 Mib 
            2 - 0.0 Mib
"""