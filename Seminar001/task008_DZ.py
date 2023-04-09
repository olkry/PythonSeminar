# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

shocoRow = int(input("Сколько в шоколадке линий? Напиши тут "))
shocoColumn = int(input("Отлично, а сколько столбиков? Напиши тут "))
shocoYouLike= int(input("Сколько долек хочешь взять? "))

if (shocoYouLike >= shocoRow or shocoYouLike >= shocoColumn) and shocoYouLike <= shocoRow * shocoColumn:
    if shocoYouLike == shocoRow * shocoColumn: print("Бери всё) Задача: НЕТ")
    if (shocoYouLike % shocoRow == 0 or shocoYouLike % shocoColumn == 0) and shocoYouLike < shocoRow * shocoColumn:
        print("Сие действо удобоворимо! Задача: ДА")
    else:
        print("Одним надломом не обойтись. Задача: НЕТ")
elif shocoYouLike < shocoRow or shocoYouLike < shocoColumn:
    print("Маловат кусочек. Задача: НЕТ")
else:
    print("Так вообще не получиться! Задача: НЕТ")
