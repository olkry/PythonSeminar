# Даны два списка чисел. Требуется вывести те элементы
# первого списка (в том порядке, в каком они идут в первом
# списке), которых нет во втором списке. Пользователь вводит
# число N - количество элементов в первом списке, затем N
# чисел - элементы списка. Затем число M - количество
# элементов во втором списке. Затем элементы второго списка
import random

print(list_1 := [random.randint(0, 10) for _ in range(10)])
print(list_2 := [random.randint(0, 10) for _ in range(5)])
print([i for i in list_1 if i not in list_2])

# # Что написано:
# в 9 строке через моржёвый оператор забиваем в переменную рандом из 10 симвалов и выводим сразу.
# в 10, тожесамое, но с 5 элементами.
# 11 строка расписана ниже

new_list = []
for i in list_1:
    if i not in list_2:
        new_list.append(i)

