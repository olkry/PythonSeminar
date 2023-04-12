# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх
# одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

import random

coin_num = int(input('Сколько на столе монеток? '))
coin_toss_eagle = 0
coin_toss_front = 0
count = 1
while count <= coin_num:
    coin_on_table = random.randint(0, 1)
    print(count, "монетка выпала", 'Орлом' if coin_on_table == 0 else 'Решкой')
    if coin_on_table == 1:
        coin_toss_front += 1
    else:
        coin_toss_eagle += 1
    count += 1
print()
print(f'Чтобы все монетки лежали Решкой, переверните {coin_toss_eagle} монет')
print(f'Чтобы все монетки лежали Орлом, переверните {coin_toss_front} монет')

# # Эталонное решение
#
# n = int(input('fd'))
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         count_zero += 1
#     else:
#         count_one += 1
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)
