# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random

#
# list_lenth, serch_num = int(input('Какой длины сгенерировать список? ')), \
#                         int(input('Ближайшее к какому числу ищём? '))
# list_for_task = [random.randint(1, 99) for i in range(list_lenth)]
# print('Сгенерирован список', *list_for_task)
# nearest_num = list_for_task[0]
# min_range = nearest_num - serch_num
# if min_range < 0:
#     min_range *= -1
# for i in list_for_task:
#     count_range = i - serch_num
#     if count_range < 0:
#         count_range *= -1
#     if count_range < min_range:
#         min_range = count_range
#         nearest_num = i
# print(f'{nearest_num} - ближайшее к загаданному числу {serch_num} в списке')

#  Or

my_list = [random.randint(0, 50) for _ in range(20)]
print(my_list)
number = int(input('Введите искомое число: '))

count_num = my_list.count(number)

closet = my_list[0]
if count_num == 0:
    for num in my_list:
        if abs(number - num) < abs(number - closet):
            closet = num

print(
    f'Число {number} встречается в списке {count_num} раз' if count_num > 0 else
    f'{closet} - ближайшее к загаданному числу {number} в списке')
