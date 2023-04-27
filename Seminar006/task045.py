# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# def find_dividers(number: int) -> list:
#     return [i for i in range(1, number // 2 + 1) if number % i == 0]
#
#
# for i in range(1, 10000):
#     sum_i_dividers = sum(find_dividers(i))
#     for j in range(i + 1, 10000):
#         if j == sum_i_dividers and i == sum(find_dividers(j)):
#             print(i, j)

# OR

# def divisors_sum(number):
#     return sum(i for i in range(1, (number // 2) + 1) if number % i == 0)
#
#
# max_number = 10000
# pairs = {}
# for i in range(1, max_number + 1):
#     aggr = divisors_sum(i)
#     if i == divisors_sum(aggr) and i != aggr:
#         if i and aggr not in pairs:
#             pairs[i] = aggr
# print(pairs)

# ORRRR

def sum_dividers(number: int) -> int:
    sum_div = 0
    for div in range(1, number // +1):
        if not number % div:
            sum_div += div
    return sum_div


all_numbers = {number: sum_dividers(number) for number in range(10000)}

for num in range(10000):
    if num == all_numbers.get(all_numbers.get(num)) and num <all_numbers.get(num):
        print(num, sum_dividers(num), sep='\U0001F91D ')
