# Задача о раскраске графа

# Создаем граф в виде списка смежности
graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [2, 3, 5],
    5: [4]
}

# Функция для раскраски графа
def greedy_coloring(graph):
    color_map = {}  # Словарь для отображения вершины в цвет

    for node in graph:
        neighbor_colors = set()  # Множество цветов соседей текущей вершины

        # Проверяем цвета соседей
        for neighbor in graph[node]:
            if neighbor in color_map:
                neighbor_colors.add(color_map[neighbor])

        # Находим первый доступный цвет для текущей вершины
        color = 1
        while color in neighbor_colors:
            color += 1

        color_map[node] = color  # Присваиваем вершине найденный цвет

    return color_map

# Получаем раскраску графа
coloring = greedy_coloring(graph)

# Выводим раскраску вершин графа
for node, color in coloring.items():
    print(f"Вершина {node} раскрашена в цвет {color}")