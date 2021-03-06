"""5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и
заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке."""


def show_ascii(n=32, count=0):
    if n == 128:
        print()
    elif count == 10:
        print()
        return show_ascii(n, count=0)
    else:
        print(f'{n} - {chr(n)}', end=' ')
        return show_ascii(n + 1, count + 1)


if __name__ == '__main__':
    show_ascii()
