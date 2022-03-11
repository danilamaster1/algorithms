"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.

Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import time

# 2. Посчитать четные и нечетные цифры введенного натурального числа.

start = time.time()


# При значении (124567353) время выполнения: 1.1c
# O(n!)
def counter(num, even=0, odd=0):
    if num == 0:                                                # O(1)
        return f'Четных: {even}, нечетных: {odd}'               # O(1)
    else:
        if num % 10 % 2 == 0:                                   # O(1)
            return counter(num // 10, even + 1, odd)            # O(n!)
        return counter(num // 10, even, odd + 1)                # O(n!)


if __name__ == '__main__':
    print(counter(int(input('Введите натуральное число: '))))
    print(f'{time.time() - start} секунд')

start = time.time()


# При значении (124567353) время выполнения: 0.8с
# O(n)
def counter_2(num):
    even = 0                                          # O(1)
    odd = 0                                           # O(1)
    while num > 0:                                    # O(n)
        if num % 10 % 2 == 0:                         # O(1)
            even += 1                                 # O(1)
            num //= 10                                # O(1)
        else:
            odd += 1                                  # O(1)
            num //= 10                                # O(1)
    return f'Четных: {even}, нечетных: {odd}'         # O(1)


if __name__ == '__main__':
    print(counter_2(int(input('Введите натуральное число: '))))
    print(f'{time.time() - start} секунд')



