# Функции высшего порядка принимают в качестве аргументов другие функции.
# map - применяет функцию ко всем элементам коллекции
# my_string = '1234567890'
# # my_string = list(my_string)  # перевод строки в символы, но остаются str
# # print(my_string)
# # Чтобы перевести в int, например сумму всех найти
# # for i in range(len(my_string)):
# #     my_string[i] = int(my_string[i])   # Посимвольный перевод из str в int
# # print(my_string)
# # Как это делает map
# # my_string = list(map(int, my_string))
# # print(my_string)
# # В map можно использовать и лямбда функцию и аргумент - функцию
# my_string = list(map(lambda x: x + '1', my_string))  # Прибавим 1 на конец каждого символа в str
# print(my_string)

# filter - проверяет на TRUE/False
# my_string = '123dfl456dsi7890'
# my_string = list(my_string)
# print(my_string)
#
# # my_string = list(filter(lambda x: x.isdigit(), my_string)) #  Удалит все символы, кроме цифр
# # print(my_string)
#
# # my_string = list(filter(lambda x: not x.isdigit(), my_string)) #  Удалит все символы, кроме букв
# # print(my_string)


# enumerate - комплектация коллекции, кортежа
# my_string = '123dfl456dsi7890'
# my_string = list(my_string)
# print(my_string)
#
# for i, item in enumerate(my_string, 1):   # число 1 в данном случае показывает с какого числа пойдёт отсчёт
#     print(i, item)

# zip - совмещение двух списков в кортеж по минимальному элементу

# my_num = '1234567890'
# mt_let = 'asdfghjkly'
# list_1 = list(my_num)
# list_2 = list(mt_let)
# print(list_1)
# print(list_2)
# # # Без zip
# # new_list = []
# # for i, item in enumerate(list_1):
# #     new_list.append((list_1[i], list_2[i]))
# # print(new_list)
#
# # # Через zip
# # new_list = []
# # new_list = list(zip(list_1, list_2))
# # print(new_list)

# # Если необходимо по большему списку идти нужно импортировать zip_longest
# from itertools import zip_longest
# my_num = '1234'
# mt_let = 'asdfghjkly'
# list_1 = list(my_num)
# list_2 = list(mt_let)
# print(list_1)
# print(list_2)
#
# new_list = list(zip_longest(list_1, list_2, fillvalue='Ничего'))  # fillvalue заменяет NONE на вписанное слово
# print(new_list)

# lambda

# def is_digit(num: str):
#     return num.isdigit()
# # Или
#
# lambda x: x.isdigit()
