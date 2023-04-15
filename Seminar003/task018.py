# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random

list_lenth, serch_num = int(input('Какой длины сгенерировать список? ')), \
                        int(input('Ближайшее к какому числу ищём? '))
list_for_task = [random.randint(1, 99) for i in range(list_lenth)]
print('Сгенерирован список', *list_for_task)
nearest_num = list_for_task[0]
min_range = nearest_num - serch_num
if min_range < 0:
    min_range *= -1
for i in list_for_task:
    count_range = i - serch_num
    if count_range < 0:
        count_range *= -1
    if count_range < min_range:
        min_range = count_range
        nearest_num = i
print(f'{nearest_num} - ближайшее к загаданному числу {serch_num} в списке')
