# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять списки и использовать циклы
# (даже для ввода и вывода).

# def sequence(num: int, s='') -> str:
#     if num != 0:
#         return sequence(num-1, s + str(num) + ' ')
#     else:
#         return s
#
# num = int(input('Enter number: '))
# print(sequence(num))


# def print_sequence(num: int) -> None:
#     print(num, end=' ')
#     if num != 0:
#         print_sequence(num - 1)
#
#
# number = int(input('Enter number: '))
# print_sequence(number)

# Another solution

number = int(input('Enter number: '))


def revers_sequence(n: int):
    if n == 1:
        return n
    else:
        return f'{n} {revers_sequence(n - 1)}'


print(revers_sequence(number))
