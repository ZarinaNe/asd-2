# 12.Реализовать алгоритм Кнута-Морриса-Пратта для поиска по образцу

def compute_prefix_function(pattern):

    # Функция для вычисления префикс-функции для заданной строки поиска (образца).

    prefix_function = [0] * len(pattern)
    j = 0  # Индекс, с которого начинается сравнение символов

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_function[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        prefix_function[i] = j

    return prefix_function

def search_pattern_with_kmp(file_name, pattern):

    # Функция для поиска образца в файле с использованием алгоритма Кнута-Морриса-Пратта (KMP).

    try:
        # Чтение строки из файла
        with open(file_name, 'r') as file:
            text = file.read()

        # Вычисление префикс-функции для образца
        prefix_function = compute_prefix_function(pattern)

        j = 0  # Индекс, с которого начинается сравнение символов
        indices = []

        # Проход по символам исходной строки
        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = prefix_function[j - 1]

            if text[i] == pattern[j]:
                j += 1

            if j == len(pattern):
                indices.append(i - len(pattern) + 1)
                j = prefix_function[j - 1]

        return indices

    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
        return []

# Ввод строки поиска с клавиатуры
search_string = input("Введите строку для поиска: ")

# Ввод имени файла с данными
file_name = 'input.txt'

# Вызов функции поиска
result = search_pattern_with_kmp(file_name, search_string)

if result:
    print(f"Образец найден в позициях: {result}")
else:
    print("Образец не найден в файле.")