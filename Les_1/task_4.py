from random import randint


def rand_symbol(start, end):
    if start.isalpha() and end.isalpha():
        return f'{chr(randint(ord(start), ord(end)))}'
    return f'{randint(int(start), int(end))}'


print(rand_symbol(input('Введите начало диапазона (целое, вещественное, англ алфавит): '),
                  input('Введите конец диапазона:')))




