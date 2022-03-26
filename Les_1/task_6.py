"""6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""


class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


def find_letter(ord_num):
    try:
        if 97 <= int(ord_num) < 122:
            return chr(int(ord_num))
        else:
            raise MyErr('Введите число соответсвующее позиции в алфавите')
    except (ValueError, MyErr) as err:
        return err


print(find_letter(input('Введите номер позиции буквы англ алфавита: ')))
