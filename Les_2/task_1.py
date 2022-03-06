"""1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа
'0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю
о невозможности деления на ноль, если он ввел 0 в качестве делителя."""


def calc(str_equation):
    list_equation = str_equation.split(' ')
    if list_equation[0] == '0' and len(list_equation) == 1:
        print('Конец')
    else:
        try:
            x = float(list_equation[0])
            y = float(list_equation[2])
            operand = list_equation[1]
        except (ValueError, IndexError):
            print('Некорректное уравнение!')
            return calc(input('Введите уравнение типа x + y (0 для выхода): '))

        if operand == '+':
            print(x + y)
            return calc(input('Введите уравнение типа x + y (0 для выхода): '))
        elif operand == '-':
            print(x - y)
            return calc(input('Введите уравнение типа x + y (0 для выхода): '))
        elif operand == '*':
            print(x * y)
            return calc(input('Введите уравнение типа x + y (0 для выхода): '))
        elif operand == '/':
            try:
                result = x / y
            except ZeroDivisionError:
                print('Деление на ноль!')
                return calc(input('Введите уравнение типа x + y (0 для выхода): '))
            else:
                print(result)
                return calc(input('Введите уравнение типа x + y (0 для выхода): '))
        else:
            print('Неверный знак!')
            return calc(input('Введите уравнение типа x + y (0 для выхода): '))


if __name__ == '__main__':
    calc(input('Введите уравнение типа x + y (0 для выхода): '))
