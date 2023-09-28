# Реализовать алгоритм Бойера-Мура для поиска по образцу

def build_bad_character_table(pattern):
    # Создаем словарь для таблицы плохих символов
    bad_character_table = {}
    pattern_length = len(pattern)

    # Заполняем таблицу плохих символов для всех символов, кроме последнего
    for i in range(pattern_length - 1):
        char = pattern[i]
        bad_character_table[char] = pattern_length - i - 1

    # Для последнего символа заполняем таблицу полностью
    last_char = pattern[-1]
    bad_character_table[last_char] = max(1, pattern_length)

    return bad_character_table

def boyer_moore_search(text, pattern):
    # Получаем длины текста и образца
    text_length = len(text)
    pattern_length = len(pattern)

    # Строим таблицу плохих символов
    bad_character_table = build_bad_character_table(pattern)

    # Начальная позиция поиска
    position = pattern_length - 1

    while position < text_length:
        # Индекс для сравнения символов в образце
        i = pattern_length - 1

        while i >= 0 and text[position] == pattern[i]:
            position -= 1
            i -= 1

        if i == -1:
            # Образец найден, вернем его позицию
            return position + 1

        # В противном случае, перемещаем позицию в соответствии с таблицей плохих символов
        bad_char = text[position]
        if bad_char in bad_character_table:
            bad_char_shift = bad_character_table[bad_char]
        else:
            bad_char_shift = pattern_length
        position += max(1, bad_char_shift)

    # Образец не найден
    return -1

# Функция для чтения текста из файла
def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Запрос образца с клавиатуры
pattern = input('Введите образец для поиска: ')

# Задаем имя входного файла
input_filename = 'input.txt'

# Читаем текст из файла
text = read_text_from_file(input_filename)

# Вызываем функцию поиска
result = boyer_moore_search(text, pattern)

if result != -1:
    print(f'Образец найден на позиции {result}')
else:
    print('Образец не найден')