# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, x=','):# cама функция
    y = group1.split(x) # 1 группа
    z = group2.split(x) # 2 группа
    common = [] #создание списка
    for participant in y: # для участников в 1 группе
        if participant in z and participant not in common: # если участник из первой группы и 2 , но при этом не в новом списке
            common.append(participant) # добавляем его в новый список
    common.sort() # сортировка в алфавитном порядке
    return common


participants_1_group = "Иванов|Петров|Сидоров" # 1 группа
participants_2_group = "Петров|Сидоров|Смирнов" # 2 группа
print(find_common_participants(participants_1_group, participants_2_group, '/'))

# TODO Провеьте работу функции с разделителем отличным от запятой
