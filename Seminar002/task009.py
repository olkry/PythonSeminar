# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while


# number = int(input('Введите число'))
#
# factor = 1
# i = 1
#
# while i <= number:
#     factor *= i
#     i += 1
# # Выше сокращенно записан код:
# #     factor = factor * i
# #     i = i + 1
# print(factor)

# или

number = int(input('Введите число'))

factor = 1
i = 1

for i in range(1, number + 1):   #renge(start, finish, step)
    factor *= i

print(factor)
