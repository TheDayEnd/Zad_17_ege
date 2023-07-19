with open('17_easy.txt') as f:  # открытие файла
    m = [int(i) for i in f]  # создание массива со всеми числами в файле

# Инициализируем переменную для хранения количества пар и минимального куба полусуммы модулей элементов пары
count_pairs = 0
min_cube = float('inf')

# Ищем максимальный элемент последовательности, оканчивающийся на 73
max_elem = max(filter(lambda x: x % 100 == 73, m))
print(max_elem)
# Проходим по списку m и ищем пары, удовлетворяющие условию задачи
for i in range(len(m) - 1):
    if abs(m[i]) % 10 == 6 and abs(m[i+1]) % 10 == 6:
        half_sum = (abs(m[i]) + abs(m[i+1])) / 2
        if half_sum ** 3 > max_elem ** 2:
            count_pairs += 1  # счетчик пар при нахождении пары увеличивается
            min_cube = min(min_cube, half_sum ** 3)  # минимальный куб полусуммы

# Выводим результат на экран
print(count_pairs, min_cube)