from methods import *

print("Добро пожаловать!", "Телефонная книга версии pre.alpha.0.055. к вашим услугам.",
      "В настоящее время доступны следующие команды:", "1. Просмотреть контакты", sep='\n')
choice = int(input('Введите команду:\t'))

if choice == 1:
    look_data(read_data("input_data.txt"))
elif choice == 2:
    add_data("input_data.txt")
else:
    print("Неверная команда!!!")
