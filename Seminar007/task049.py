# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
import random
from math import pi

#
#
# def generate_sequence_of_orbit(count_of_orbit: int) -> list[tuple[int,int]]:
#     result = [(random.randint(1,10), random.randint(1,10))for _ in range(count_of_orbit)]
#     return result
#
#
# def find_farthest_orbit(list_of_orbit: list[tuple[int, int]]) -> tuple[int, int]:
#     squares = [(i, e[0]*e[1]) for i, e in enumerate(list_of_orbit) if e[0] != e[1]]
#     max_squares = max(squares, key=lambda x: x[1])
#     return list_of_orbit[max_squares[0]]
#
#
# orbits = generate_sequence_of_orbit(10)
# print(orbits)
# print(find_farthest_orbit(orbits))

# Ещё вариант

# num = int(input('Enter a number of planet:\t'))
# orbits = [(random.randint(1, 10), random.randint(1, 10)) for i in range(num)]
# print(f'the list: {orbits}')
#
# ell_sq = lambda rad: pi * rad[0] * rad[1]
# orbits_sq = [ell_sq(orbits[i]) for i in range(len(orbits))]
#
# print(orbits[max([val, ind] for ind, val in enumerate(orbits_sq) if orbits[ind][0] != orbits[ind][1])[1]])

# Ещё вариант:

