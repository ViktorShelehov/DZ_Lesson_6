# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progression(a1, d, n):
    progression = []
    for i in range(n):
        an = a1 + (i * d)
        progression.append(an)
    return progression

# Ввод данных с клавиатуры
a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов: "))

# Заполнение массива арифметической прогрессией
progression = arithmetic_progression(a1, d, n)

# Вывод прогрессии
print("Арифметическая прогрессия:")
for element in progression:
    print(element)