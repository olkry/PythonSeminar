# Методы для работы программы.

def read_data(phones_list):
    with open(phones_list, 'r', encoding='utf-8') as file:
        data_list = file.readlines()
        data_list = [x.rstrip().split(':') for x in data_list]
    return data_list


def look_data(phones):
    for i, item in enumerate(phones, 1):
        print(i, ', '.join(item))


def add_data(phones_list):
    with open(phones_list, 'a', encoding='utf-8') as file:
        name, phone, comment = input("Введите ФИО:\t"), input("Введите телефон:\t"), \
            input("Введите комментарий:\t")
        string = [name+':', phone+':', comment]
        file.writelines(string)

# add_data("test.txt")
# look_data(read_data("test.txt"))


