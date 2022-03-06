"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""

import random

arr = [random.randint(-99, 99) for _ in range(50)]
print(arr)

min_index = 0

for i in arr:
    if arr[min_index] > i:
        min_index = arr.index(i)

if arr[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {arr[min_index]}.',
            f'Находится в массиве на позиции {min_index}')
