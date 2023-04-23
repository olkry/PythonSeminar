# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

import random

# marks = [random.randint(1, 5) for _ in range(10)]
# print(marks)
# max_marks = max(marks)
# min_marks = min(marks)
# for i in range(len(marks)):
#     if marks[i] == max_marks:
#         marks[i] = min_marks
# print(marks)

# Another solution

number = int(input('Number of user ratings: '))
rating_list = []

for i in range(number):
    rating_list.append(random.randint(1, 5))
print(rating_list)

max_rating = max(rating_list)
min_rating = min(rating_list)

for i in range(number):
    if rating_list[i] == max_rating:
        rating_list[i] = min_rating
print(rating_list)