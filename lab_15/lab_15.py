# Задача о раскраске графа

# Создаем граф в виде словаря, где ключи - вершины, а значения - их соседи
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 4],
    4: [2, 3, 5],
    5: [2, 4],
    6: []
}

# Создаем словарь для хранения цветов вершин
coloring = {}

# Упорядочиваем вершины по невозрастанию степени
nodes_sorted_by_degree = sorted(graph.keys(), key=lambda x: -len(graph[x]))

# Начинаем окраску с первой вершины
coloring[nodes_sorted_by_degree[0]] = 1

current_color = 0
# Повторяем окраску до тех пор, пока все вершины не будут окрашены
while len(coloring) < len(graph):
    current_color += 1  # Выбираем следующий цвет
    for node in nodes_sorted_by_degree:
        if node not in coloring:
            adjacent_colors = {coloring[neighbor] for neighbor in graph[node] if neighbor in coloring}
            if current_color not in adjacent_colors:
                coloring[node] = current_color

# Выводим окраску вершин
print("Результат раскраски:")
for node, color in coloring.items():
    print(f"Вершина {node} окрашена в цвет {color}")