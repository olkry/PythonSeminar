# Методы для работы программы.

def read_data(phones_list):  # Считывает данные из файла
    with open(phones_list, 'r', encoding='utf-8') as file:
        data_list = file.readlines()
        data_list = [x.rstrip().split(':') for x in data_list]
    return data_list


def look_data(phones):  # Выводит данные из принимаемого списка
    for i, item in enumerate(phones, 1):
        print(i, ', '.join(item))


def add_data(phones_list):  # Добовляет данные в список
    with open(phones_list, 'a', encoding='utf-8') as file:
        name, phone, comment = input("Введите ФИО:\t"), input("Введите телефон:\t"), \
            input("Введите комментарий:\t")
        string_add = [name + ':', phone + ':', comment + '\n']
        file.writelines(string_add)


def del_data(phone_list, del_line):
    with open(phone_list, 'r', encoding='utf-8') as file:
        losting_data = file.readlines()
        losting_data.pop(del_line - 1)
    with open(phone_list, 'w', encoding='utf-8') as file:
        file.writelines(losting_data)


def upd_data(phone_list, upd_line, new_data):
    with open(phone_list, 'r', encoding='utf-8') as file:
        upd_list = file.readlines()
        upd_list = [x.rstrip().split(':') for x in upd_list]
    upd_list[upd_line - 1] = new_data
    with open(phone_list, 'w', encoding='utf-8') as file:
        for i in upd_list:
            file.writelines(':'.join(i) + '\n')


# look_data(read_data('test.txt'))
# name, phones, comment = input("Введите ФИО:\t"), input("Введите телефон:\t"), \
#     input("Введите комментарий:\t")
# string_upd = [name, phones, comment]
# upded_line = int(input('Напишите номер контакта, для удаления, или нажмите 0, чтобы прервать операцию.\t'))
# upd_data('test.txt', upded_line, string_upd)
# look_data(read_data('test.txt'))
