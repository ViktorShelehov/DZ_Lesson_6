# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Заданный диапазон от -3 до 5
def find_indexes(array, min_value, max_value):
    indexes = []
    for i in range(len(array)):
        if min_value <= array[i] <= max_value:
            indexes.append(i)
    return indexes

# Пример использования
my_list = [2, -1, 4, 6, 3, -2, 0, 1]
min_value = -3
max_value = 5

result = find_indexes(my_list, min_value, max_value)
print("Индексы элементов в заданном диапазоне:")
print(result)