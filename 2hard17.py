with open('17_hard.txt') as f:  # открытие файла
    m = [int(i) for i in f]  # создание массива со всеми числами в файле


def count_dil(number):
    # Функция для подсчета количества делителей числа (включая 1 и само число)
    count = 0
    for i in range(1, abs(number) + 1):
        if number % i == 0:
            count += 1
    return count


def identical2(number):
    # Функция для проверки, есть ли в числе 2 цифры, которые одинаковы
    num_str = str(abs(number))
    return len(set(num_str)) == 2

elems = []
for i in m:
    if identical2(i):
        elems.append(i)
max_elem = max(elems)


min_para = []  # массив с минимальными элементами из пары
result = []  # массив с суммой модулей элементами пары

for i in range(len(m) - 1):  # цикл перебора пар начинается с 0 до длины массива m уменьшеннего на 1
    e1 = m[i]  # первый элемент пары
    e2 = m[i + 1]  # второй элемент пары
    if count_dil(e1) == count_dil(e2):  # проверка на равное количество делителей
        if e1 * e2 > 0:  # являются ли числа с одинаковым знаком
            # при умножении чисел с одинаковым знаком всегда будет число положительное
            # это и проверяем
            if abs(e1) + abs(e2) < max_elem:  # проверка условия с макс элементом
                result.append(abs(e1) + abs(e2))  # добавление в массив суммы модулей
                min_para.append(min(e1, e2))  # добавление в массив минимального элемента пары

# сортировка массивов
result.sort()
min_para.sort()

sr_znach = int(sum(result) / len(result))  # для нахождения ср.знач надо всю сумму поделить на количество
# sum(result) - сумма всех значений, len(result) - количество значений

print(sr_znach, min(min_para))  # вывод ответа
# возможная запись print(sr_znach, min_para[0])
