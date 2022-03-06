"""4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры."""


def sum_digit(n, count=0, num=1.0, summa=0.0):
    if count == n:
        return f'Сумма из {n} элементов = {summa}'
    return sum_digit(n, count + 1, -num/2, summa + num)


if __name__ == '__main__':
    print(sum_digit(int(input('Введите кол-во элементов: '))))
