# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# # Если записать строку слитно, можно разделить каждый список одельно:
# my_string = 'gjhlgkhjhlfldhghglkfj'
# my_list = list(my_string)
# print(my_list)
# # Если написано раздельно, надо использовать split, верхний метод посчитает засимвол пробел
# my_string = 'g j h l g k h j h l f l d h g h g l k f j'
# my_list = my_string.split()
# print(my_list)

# s = input("Введите строку ")
# chars_list = list(s)
# count = dict()
# for c in chars_list:
#     if c in count:
#         count[c] = count[c] + 1
#     else:
#         count[c] = 0
#     repeats_count = count[c]
#     print(f'{c}_{repeats_count}' if repeats_count > 0 else c, end=" ")  #END не даёт перенести строкй, добовляя пробел

# split_string = input('Введите строку: ').split()
# res = {}
# for i in split_string:
#     if i in res:
#         print(f'{i}_{res[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     res[i] = res.get(i, 0) + 1
# print('\n')


my_string = 'g j h l g k h j h l f l d h g h g l k f j'
my_list = my_string.split()
print(my_list)
dic_count = {}
for letter in my_list:
    # dic_count[letter] = dic_count.get(letter, 0) + 1
    # print(letter if dic_count.get(letter) == 1 else f'{letter}_{dic_count.get(letter) - 1}', end=' ')
# or

    print(letter if letter not in dic_count else
          f'{letter}_{dic_count.get(letter)}', end=' ')
    dic_count[letter] = dic_count.get(letter, 0) + 1

