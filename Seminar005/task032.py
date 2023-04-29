# Определить индексы элементов списка, значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)

import random

print(list_my := list(random.randint(0, 10) for _ in range(20)))
max_num = random.randint(0, 10)
min_num = random.randint(0, 10)

if max_num < min_num:
    max_num, min_num = min_num, max_num

# for i in range(len(list_my)):
#     if min_num <= list_my[i] <= max_num:
#         print(i, end=' ')


print(f'В диапозон от {min_num} до {max_num} входят индексы'
      f' {list(i for i in range(len(list_my)) if min_num <= list_my[i] <= max_num)}')
