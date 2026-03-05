list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2 # деление списка на целые части без остатка

first_team = list_players[:middle_index] # деление на две части
second_team = list_players[middle_index:] # деление на две части

print(first_team) # результат
print(second_team) # результат