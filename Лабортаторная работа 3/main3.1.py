# TODO Напишите функцию для поиска индекса товара
def find_item_index(items, target_item):#сама функция
    if target_item in items:#проверка наличия
        return items.index(target_item) #возвращаем 1 индекс
    else: #если не нашли
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан'] #список имеющихся продуктов

for find_item in ['банан', 'груша', 'персик']:#список поиска продуктов
    index_item = find_item_index(items_list, find_item) #обращение к функции
    if index_item is not None:#если найден
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:#если не найден
        print(f"Товар '{find_item}' не найден в списке.")
