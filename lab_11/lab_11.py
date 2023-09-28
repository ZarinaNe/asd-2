# Реализовать алгоритм поиска по образцу с помощью конечного автомата

# Функция для создания таблицы переходов (конечного автомата) для строки поиска
def create_transition_table(pattern):
    alphabet = set(pattern)
    table = {}
    m = len(pattern)

    for state in range(m + 1):
        table[state] = {}
        for char in alphabet:
            next_state = min(m, state + 1)
            while next_state > 0 and pattern[next_state - 1] != char:
                next_state = table[next_state - 1].get(char, 0)
            table[state][char] = next_state

    return table


# Функция для поиска образца в строке с использованием конечного автомата
def search_with_fsm(text, pattern):
    m = len(pattern)
    n = len(text)
    table = create_transition_table(pattern)
    state = 0  # начальное состояние

    for i in range(n):
        while state > 0 and text[i] != pattern[state]:
            state = table[state - 1].get(text[i], 0)

        if text[i] == pattern[state]:
            state += 1

        if state == m:
            return i - m + 1  # образец найден, возвращаем индекс начала образца в тексте

    return -1  # образец не найден


# Считываем исходную строку из файла
with open('input.txt', 'r') as file:
    text = file.read()

# Считываем строку поиска с клавиатуры
pattern = input("Введите строку поиска: ")

# Вызываем функцию поиска и выводим результат
index = search_with_fsm(text, pattern)
if index != -1:
    print(f"Образец найден в позиции {index}")
else:
    print("Образец не найден")