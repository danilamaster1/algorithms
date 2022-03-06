"""1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""


def find_sum_composition(num):
    sum_digit = 0
    compos_digit = 1
    while num > 0:
        sum_digit += num % 10
        compos_digit *= num % 10
        num //= 10
    return f'Сумма:{sum_digit}, произведение:{compos_digit}'


if __name__ == '__main__':
    print(find_sum_composition(int(input('Введите трехзначное число: '))))


