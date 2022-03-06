"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран."""


def permutation(num, result=''):
    if num == 0:
        return result
    result += str(num % 10)
    return permutation(num // 10, result)


if __name__ == '__main__':
    print(permutation(int(input('Введите число, которое хотите перевернуть: '))))
