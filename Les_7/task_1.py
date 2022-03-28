"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.

По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint


def bubble_sort(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


lst_obj = [randint(-100, 100) for _ in range(20)]
print(lst_obj)
print(bubble_sort(lst_obj))
