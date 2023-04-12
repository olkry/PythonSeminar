# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа
# X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import random
hidden_number_1, hidden_number_2 = random.randint(1, 1000), random.randint(1, 1000)
sum_number = hidden_number_1 + hidden_number_2
product_num = hidden_number_1 * hidden_number_2
print(f'Вам загадали 2 числа, сумма которых {sum_number} а произведение равно {product_num}')
count = 1
while count <= 1000000:
    if product_num / count == sum_number - count:
        num_1 = count
    count += 1
num_2 = sum_number - num_1
input('Запустить код - оракул?')
print(f'Большее загаданное число {num_1}, меньшее соответственно {num_2}')
input("Теперь давайте проверим.")
print(f"Первое загаданное число {hidden_number_1}, второе {hidden_number_2}.")

# # Эталонное решение?? не работает..
#
# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)
