"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""

my_list = [1, 4, 45, 7, 2, 6]

first_min = min(my_list)
my_list.remove(first_min)
second_min = min(my_list)

print(first_min, second_min)
