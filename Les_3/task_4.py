"""4. Определить, какое число в массиве встречается чаще всего."""

src = [44, 7, 44, 7, 23, 7, 44, 44, 3, 2, 10, 44, 44, 11]

dig_dict = {n: 0 for n in src}
for i in src:
    dig_dict[i] += 1


def get_key(dict_, value_):
    for k, v in dict_.items():
        if v == value_:
            return k


value = max(dig_dict.values())

print(f'Чаще всего встречается: {get_key(dig_dict, value)} ({value} раз)')


