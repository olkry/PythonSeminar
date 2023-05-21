# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


# Примитивное решение

# chant = input("Напишите кричалку\t").lower()
# chant_index = len(chant.split())
# vowels = {'аоиыуэ': 'vow'}
# vow_count = 0
#
# for i in chant:
#     for j in vowels:
#         if i in j:
#             vow_count += 1
#
# print('Парам пам-пам' if vow_count % chant_index == 0 else 'Пам парам')

# С функцией

# def presence_of_rhythm(word, dict, len)->str:
#     count = 0
#     for i in word:
#         for j in dict:
#             if i in j:
#                 count +=1
#     if count % len == 0:
#         return print('Парам пам-пам')
#     else:
#         return print('Пам парам')
#
#
# chant = input("Напишите кричалку\t").lower()
# vowels = {'аоиыуэ': 'vow'}
#
# presence_of_rhythm(chant, vowels, len(chant.split(' ')))

# chant = input("Напишите кричалку\t").lower()

def vowels_total(char):
    if char in 'аоиыуэ':
        return char
    else:
        return 0


chant = 'пара-реа-роам рам-пам-паепоам па-ра-пао-да'
total_wav = len(list(map(lambda x: vowels_total(x), chant)))
print('Парам пам-пам' if total_wav % len(chant.split(' ')) == 0 else 'Пам парам')
