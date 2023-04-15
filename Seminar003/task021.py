# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# my_dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
#                  {" V ": "S009"}, {" VIII ": "S007"}]
# unique_values = set()
# for element in my_dictionary:
#     for value in element.values():
#         unique_values.add(value)
# print(unique_values)

# Вариант

my_dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
                 {" V ": "S009"}, {" VIII ": "S007"}]
res = set()
for i in my_dictionary:
    for (k, v) in i.items():
        res.add(v)
print(res)
