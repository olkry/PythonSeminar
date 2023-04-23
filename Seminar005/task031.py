# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fibonacchi(n):
    if n in [0, 1]:
        return n
    return fibonacchi(n - 1) + fibonacchi(n - 2)


number_fibonnachi = int(input("Enter number fibonnachi: "))
print(f'Number №{number_fibonnachi} in the Fibonacci sequence: {fibonacchi(number_fibonnachi)}.')
