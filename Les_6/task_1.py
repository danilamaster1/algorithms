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

from sys import getsizeof
import random


# 1
def find_even_pos():
    mas_num = [random.randint(1, 100) for n in range(9)]

    mas_index = [mas_num.index(i) for i in mas_num if i % 2 == 0]

    print(getsizeof(mas_num))      # 184
    print(getsizeof(mas_index))    # 120
    return 'Массив индексов четных элементов: {}'.format(mas_index)


find_even_pos()

print('*' * 30)


# 2
def revers():
    new_num = ''

    num = str(10 ** 3)
    count = len(num)
    k = range(count)

    for i in k:
        new_num = new_num + str(int(num) % 10)
        num = int(num) // 10

    print(getsizeof(new_num))  # 53
    print(getsizeof(num))      # 24
    print(getsizeof(count))    # 28
    print(getsizeof(k))        # 48
    return new_num


revers()
