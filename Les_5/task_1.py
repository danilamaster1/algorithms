"""1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
наименования предприятий, чья прибыль ниже среднего."""

from collections import namedtuple


def profit():
    my_var = "Company"
    n = int(input("Введите кол-во предприятий: "))
    companies = namedtuple(
        my_var,
        "name period_1 period_2 period_3 period_4")
    profit_aver = {}

    for i in range(n):
        company = companies(
            name=input("Введите название компании: "),
            period_1=int(input('Введите прибыль за первый квартал: ')),
            period_2=int(input('Введите прибыль за второй квартал: ')),
            period_3=int(input('Введите прибыль за третий квартал: ')),
            period_4=int(input('Введите прибыль за четвертый квартал: ')))

        profit_aver[company.name] = (
            company.period_1 + company.period_2 +
            company.period_3 + company.period_4) / 4

    total_aver = 0
    for value in profit_aver.values():
        total_aver += value
    total_aver = total_aver / n

    for key, value in profit_aver.items():
        if value > total_aver:
            print(f"{key} - прибыль выше среднего")
        elif value < total_aver:
            print(f"{key} - прибыль ниже среднего")
        elif value == total_aver:
            print(f"{key} - средняя прибыль")


profit()
