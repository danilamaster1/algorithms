n_1, n_2, n_3 = [int(x) for x in input('Введите три числа через пробел: ').split()]

if n_2 < n_1 < n_3 or n_3 < n_1 < n_2:
    print(f'Среднее {n_1}')
elif n_1 < n_2 < n_3 or n_3 < n_2 < n_1:
    print(f'Среднее {n_2}')
else:
    print(f'Среднее {n_3}')
