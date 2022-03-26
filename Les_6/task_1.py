"""
1. Подсчитать, сколько было выделено памяти под переменные
в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
"""

from sys import getsizeof
from collections import namedtuple


#  Не оптимизированная
def num_translate():
    numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    print(getsizeof(numbers))   # 360
    return numbers.get('ten')


# Оптимизированная
def num_translate_tuple():
    dict_ = namedtuple('dict_', ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'))
    d = dict_(one='один',
              two='два',
              three='три',
              four='четыре',
              five='пять',
              six='шесть',
              seven='семь',
              eight='восемь',
              nine='девять',
              ten='десять'
    )
    print(getsizeof(d))    # 120
    return d.ten


num_translate()
num_translate_tuple()

"""
с namedtuple мы выигрываем по памяти в 3 раза
"""
