# Дан список, состоящий из целых чисел. Напишите
# программу, которая в данном списке определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в списке
# Далее записаны N чисел — элементы списка. Список
# состоит из целых чисел.

import random

print(list_input := [random.randint(0, 10) for _ in range(20)])
# count = 0
print(len([i for i in range(1, len(list_input) - 1) if list_input[i - 1] < list_input[i] > list_input[i + 1]]))
# for i in range(1, len(list_input) - 1):
#     if list_input[i - 1] < list_input[i] > list_input[i + 1]:
#         count += 1
# print(count)
