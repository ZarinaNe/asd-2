# 14.Реализовать алгоритм Рабина для поиска по образцу

# Функция для вычисления хэша строки с помощью алгоритма Рабина-Карпа
def compute_hash(text, length):
    hash_value = 0
    for i in range(length):
        hash_value += ord(text[i])  # Суммируем коды символов
    return hash_value

# Функция для обновления хэша при сдвиге окна
def update_hash(old_hash, old_char, new_char, length):
    new_hash = old_hash - ord(old_char) + ord(new_char)
    return new_hash

# Функция для поиска образца в строке с использованием алгоритма Рабина-Карпа
def rabin_karp_search(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    pattern_hash = compute_hash(pattern, pattern_length)
    text_hash = compute_hash(text, pattern_length)

    for i in range(text_length - pattern_length + 1):
        if text_hash == pattern_hash and text[i:i + pattern_length] == pattern:
            return i  # Возвращаем индекс начала совпадения

        if i < text_length - pattern_length:
            # Обновляем хэш для следующего окна
            text_hash = update_hash(text_hash, text[i], text[i + pattern_length], pattern_length)

    return -1  # Возвращаем -1, если совпадение не найдено

# Считываем исходную строку из файла
with open('input.txt', 'r') as file:
    text = file.read()

# Запрашиваем строку поиска
pattern = input("Введите строку поиска: ")

# Вызываем функцию поиска и выводим результат
result = rabin_karp_search(text, pattern)
if result != -1:
    print(f"Образец найден в позиции {result}")
else:
    print("Образец не найден")