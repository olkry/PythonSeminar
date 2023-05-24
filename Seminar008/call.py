# 1. Открыть файл (режим txt)
# 2. Сохранить файл
# 3. Показать все контакт
# 4. Добавить контакт
# 5. Найти контакт
# 6. изменить контакт
# 7. Удалить контакт
# 8. выход

# path = 'call.txt'
# data = open(path, 'w')
# for line in data:
#     print(line)
# data.close()

def open_file_read(path):
    with open(path, 'r') as file:
        mine_list = file.readlines()
        mine_list_str = [x.rstrip().split(':') for x in mine_list]
    return mine_list_str


# print(open_file_read('phones.txt'))


def open_file_write(path, list_file):
    with open(path, 'w') as file:
        file.writelines([':'.join(x) + '\n' for x in list_file])

def look_list(list_for_look):
    print([' '.join(x) for x in list_for_look], end='\n')

list_for_look = ['Ivanov', 'Ivan', '123456', 'comment'], ['Petrov', 'Petr', '456789', 'comment'], \
    ['Chudilov', 'Sasha', '987654', 'comment']

# list_file_test = [['sdfsasdf', 'asdfdf', 'dsf'], ['dsfdyd', 'afsrgsd', 'ret']]
# open_file_write('phones_test.txt', list_file_test)

look_list(list_for_look)