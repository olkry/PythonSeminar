# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# number = int(input('Введите число для проверки '))
# fibonachi1 = 0
# fibonachi2 = 1
# count = 2
# while fibonachi2 < number:
#     fibonachi3 = fibonachi1 + fibonachi2
#     fibonachi1 = fibonachi2
#     fibonachi2 = fibonachi3
#     count += 1
# if fibonachi2 == number: print(f'Порядковый номер по Фибоначчи: {count}')
# else: print(-1)

# Топ вариант:

number = int(input('Введите число для проверки '))
fibonachi_1 = 0
fibonachi_2 = 1
count = 2

while fibonachi_2 < number:
    fibonachi_1, fibonachi_2 = fibonachi_2, fibonachi_1 + fibonachi_2
    count += 1
print(count if fibonachi_2 == number else -1)
