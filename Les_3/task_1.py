"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

count = 0
for i in range(2, 100):
    inter_count = 0
    for j in range(2, 10):
        if i % j == 0:
            inter_count += 1
    if inter_count == 8:
        count += 1

print(count)

