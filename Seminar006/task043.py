# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

import random
#
print(list_input := [random.randint(0, 10) for _ in range(10)])
# print(sum(list_input.count(i) // 2 for i in set(list_input)))

count = 0
set_input = set(list_input)
print(set_input)
for i in set_input:
    count += list_input.count(i) // 2
print(count)