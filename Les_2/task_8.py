"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""


def finder_and_counter(quantity_of_digits, sequence_of_digits, digit_for_find, count=0):
    if quantity_of_digits == len(str(sequence_of_digits)) or quantity_of_digits == 0:
        if sequence_of_digits == 0:
            print(f'Цифра:"{digit_for_find}", количество: {count}')
        else:
            if digit_for_find == sequence_of_digits % 10:
                return finder_and_counter(quantity_of_digits - 1, sequence_of_digits // 10, digit_for_find, count + 1)
            return finder_and_counter(quantity_of_digits - 1, sequence_of_digits // 10, digit_for_find, count)
    else:
        print('Колличество цифр не соответствует заданой длинне последовательности!')


if __name__ == '__main__':
    finder_and_counter(
        int(input('Введите длинну последовательности чисел: ')),
        int(input('Введите последовательность чисел(1234..): ')),
        int(input('Введите цифру из последовательности для поиска и подсчета: '))
    )
