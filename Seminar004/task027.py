# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
import string

# str_split = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea " \
#             "shells on the sea shore I'm sure that the shells are sea shore shells".lower().split()
# print(str_split)
# str_cnt = {}
# for i in str_split:
#     str_cnt[i] = str_cnt.get(i, 0) + 1
# print(f"Number of words: {len(str_cnt)}")

# OR

# str_cnt = set(str_split)
# print(f"Number of words: {len(str_cnt)}")

# OR correct

# my_string = "Я пошел домой. Домой никто не пришел".replace('.', '').lower().split()
# text = set(my_string)
# print(text)
# print(len(text))

import string
# my_string = "Я пошел домой. Домой никто не пришел".lower()
# # Удалим все символы в тексте следующим методом
# for ch in string.punctuation:  #string.punctuation - содержит в себевсе символы !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#     my_string = my_string.replace(ch, ' ')
# text = set(my_string.split())
# print(text)
# print(len(text))

print(string.digits)  #все цифры 0123456789
print(string.printable)  #все символы 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
print(string.ascii_letters)  #Все буквы abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.hexdigits)  #Шеснадцатеричная система 0123456789abcdefABCDEF

str_pun = string.punctuation.replace("'", '').replace('@', '')  #Удаление знака апострафа и собачки из списка
print(str_pun)