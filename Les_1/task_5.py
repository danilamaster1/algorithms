def find_letter_info(first_letter, second_letter):
    between = ord(second_letter) - ord(first_letter) - 1
    return f'{ord(first_letter)}, {ord(second_letter)}. Букв между ними: {between}'


print(find_letter_info(input('Введите букву алфавита: '),
                       input('Введите вторую букву алфавита в порядке возрастания: ')))

