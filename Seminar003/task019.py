# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# k = int(input('Введите сдвиг:'))
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = my_list[-k:] + my_list[:-k]
# print(new_list)

# Ещё вариант:

my_list = [i for i in range(10)]
print(my_list)
shift = int(input("На сколько сдвигаем вправо? "))

for _ in range(shift):
    my_list.insert(0, my_list.pop())  # Берёт элемент с конца и ставит на нулевую позицию

print(my_list)
