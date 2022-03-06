"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random


def switch(arr):
    print(arr)

    max_ = max(arr)
    min_ = min(arr)

    min_index = arr.index(min_)
    max_index = arr.index(max_)
    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
    print(arr)


list_ = [random.randint(0, 99) for _ in range(10)]
switch(list_)
