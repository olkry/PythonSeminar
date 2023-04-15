# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

import random

wotermellon_num = int(input('Перед вами в ряд стоят арбузы, сколько их: '))
max_weight = 0
min_weight = 30
count = 1
while count <= wotermellon_num:
    watermellon = random.randint(3, 30)
    print(f'Вес арбуза {count}: {watermellon}')
    if watermellon < min_weight:
        min_weight, number_min = watermellon, count
    if watermellon > max_weight:
        max_weight, number_max = watermellon, count
    count += 1
print(f'Иван взял для себя {number_max} арбуз весом {max_weight} кг.')
print(f'Тёще взял {number_min} арбуз весом {min_weight} кило.')
