"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

some_set = set()
S = "papa"
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        if S[i:j] != S:
            some_set.add(hashlib.sha256(S[i:j].encode()).hexdigest())
            print(S[i:j], end=' ')
print(f'\n{some_set}')
print(f'Количество элементов в множестве: {len(some_set)}')
