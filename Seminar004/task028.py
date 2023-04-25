# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

first_number, second_number = int(input('Enter first nimber: ')), \
    int(input('Enter second number: '))


def product_numbers(number_a, number_b):
    if number_b > 0:
        return product_numbers(number_a + 1, number_b - 1)
    return number_a


print(product_numbers(first_number, second_number))
