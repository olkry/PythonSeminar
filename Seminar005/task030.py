#  Заполните список элементами арифметической прогрессии. Её
# первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


start_num, difference, elements_amount = int(input('Enter the element to start counting from: ')), \
    int(input('Enter stride length: ')), int(input('Enter the number of elements: '))

for i in range(elements_amount):
    print(start_num + i * difference)
