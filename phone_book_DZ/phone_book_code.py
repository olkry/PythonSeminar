from methods import *

print("Добро пожаловать!", "Телефонная книга версии pre.alpha.0.055. к вашим услугам.",
      "В настоящее время доступны следующие команды:", "1. Просмотреть контакты", '2. Добавить новый контакт',
      '3. Изменить контакт', '4. Удалить контакт', "0. Завершить работу программы", sep='\n')
choice = int(input('Введите команду:\t'))

if choice == 1:
    print()
    look_data(read_data("input_data.txt"))
    print()
    input("Нажмите любую клавышу для завершения")

elif choice == 2:
    add_data("input_data.txt")
    print()
    print('Данные успешно сохранены')
    print()
    choice_count = int(
        input('Если желате просмотреть список контактов, нажмите 1, нажмите 0 - закрыть программу.\t'))
    if choice_count == 1:
        look_data(read_data("input_data.txt"))
        print()
        input("Нажмите любую клавышу для завершения")

    else:
        exit()

elif choice == 3:
    look_data(read_data("input_data.txt"))
    print()
    upded_line = int(input('Напишите номер контакта, для редактирования, или нажмите 0, чтобы прервать операцию.\t'))
    if upded_line == 0:
        print('Программа завершена, нажмите любую клавишу')
        exit()
    else:
        name, phones, comment = input("Введите новое ФИО для контакта:\t"), input("Введите новый телефон:\t"), \
            input("Введите новый комментарий:\t")
        string_upd = [name, phones, comment]
        upd_data("input_data.txt", upded_line, string_upd)
        print("Успешно обновленно.")
        choice_count = int(
            input('Если желате просмотреть список контактов, нажмите 1, или 0 - закрыть программу.\t'))
        if choice_count == 1:
            look_data(read_data("input_data.txt"))
            print()
            input("Нажмите любую клавишу для завершения")
        else:
            exit()

elif choice == 4:
    look_data(read_data("input_data.txt"))
    print()
    delited_line = int(input('Напишите номер контакта, для удаления, или нажмите 0, чтобы прервать операцию.\t'))
    if delited_line == 0:
        print('Программа завершена, нажмите любую клавишу')
        exit()
    else:
        del_data("input_data.txt", delited_line)
        print('Данные успешно сохранены')
        choice_count = int(
            input('Если желате просмотреть список контактов, нажмите 1, или 0 - закрыть программу.\t'))
        if choice_count == 1:
            look_data(read_data("input_data.txt"))
            print()
            input("Нажмите любую клавишу для завершения")
        else:
            exit()


elif choice == 0:
    print('Всего доброго!')

else:
    print("Неверная команда!!!")
