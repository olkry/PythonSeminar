# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

raised_number, degree = int(input('Enter the number to be raised to the power: ')), \
                        int(input('enter the degree of the number: '))


def exponentiation(num, deg):
    if num == 0:
        return 0
    elif deg == 0 or num == 1:
        return 1
    else:
        return num * exponentiation(num, deg - 1)


print(f'The number {raised_number} to the power of {degree} is {exponentiation(raised_number, degree)}')
