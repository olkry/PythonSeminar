# Дан список, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов списка, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# my_list = [0, -1, 5, 2, 3, 4, 5, 6, 4, 7, 2, 3, 4, 7, 6, 2]
# count = 0
# for i in range(1, len(my_list)):
#     if my_list[i] < my_list[i - 1]:
#         count += 1
# print(count)

# Ещё вариант с рандомом

import random

list_my = [random.randint(0, 10) for i in range(10)]
print(list_my)
count = 0
for i in range(1, len(list_my)):
    if list_my[i] > list_my[i-1]:
        count += 1
print(count)
