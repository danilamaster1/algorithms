"""2. Посчитать четные и нечетные цифры введенного натурального числа."""


def counter(num, even=0, odd=0):
    if num == 0:
        return f'Четных: {even}, нечетных: {odd}'
    else:
        if num % 10 % 2 == 0:
            return counter(num // 10, even + 1, odd)
        return counter(num // 10, even, odd + 1)


if __name__ == '__main__':
    print(counter(int(input('Введите натуральное число: '))))

