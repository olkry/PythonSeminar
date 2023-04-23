# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# def prime_number(n, div):
#     if div == n // 2 + 1:
#         print('YES')
#     elif n % div == 0:
#         print('no')
#     else:
#         prime_number(n, div + 1)
#
#
# value = int(input('Enter number: '))
# prime_number(value, 2)

# Another solution

# value = int(input('Enter number: '))
#
# def prime_number(num):
#     for i in range(2,num//2+1):
#         if num%i == 0:
#             return print('NO')
#     return print("YES")
#
#
# prime_number(value)


# Another solution, teacher's decision

def is_simple(num: int) -> bool:
    if num in [1, 2]:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, num // 2 + 1, 2):
            if num % i == 0:
                return False
    return True


num = int(input('Введите число: '))
print(f'Число {num} ' + ('простое' if is_simple(num) else 'составное'))
