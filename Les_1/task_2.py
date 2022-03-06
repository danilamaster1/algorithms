bit_and = 5 & 6
bit_or = 5 | 6
bit_xor = 5 ^ 6

left_shift = 5 << 2
# 101 << 2 == 10100 == 40
rigth_shift = 5 >> 2
# 101 >> 2 == 1 == 1


if __name__ == '__main__':
    print(f'{bit_and}\n{bit_or}\n{bit_xor}')
    print(f'Left:{left_shift}\nRight:{rigth_shift}')




