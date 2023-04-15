# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random

list_lenth, serch_num = int(input('Какой длины сгенерировать список? ')), \
                        int(input('Какое число ищём? '))
list_for_task = [random.randint(0, 10) for i in range(list_lenth)]
print(f'Сгенерирован список {list_for_task}')
count = 0
for i in list_for_task:
    if i == serch_num:
        count += 1
print(f'Число {serch_num} в списке встречается {count} раз')
