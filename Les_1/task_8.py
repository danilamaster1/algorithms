"""8. Определить, является ли год, который ввел пользователем, високосным или невисокосным."""

def year_checker(user_year):
    if user_year % 400 == 0 or user_year % 4 == 0 and user_year % 100 != 0:
        return f'Год {user_year} високосный'
    else:
        return f'Год {user_year} невисокосный'


print(year_checker(int(input('Введите год: '))))
