# Поиск в ширину
# 2.Найти в заданном графе кратчайшие пути из заданной вершины до всех остальных вершин с помощью поиска в ширину
# 3.Найти в заданном графе количество и состав компонент связности с помощью поиска в ширину.

# Код читает гцраф из файла, выполняет поиск в ширину с указанной начальной вершиной и записывает результаты в файл.

from collections import deque

# Функция для выполнения поиска в ширину (BFS)
def bfs(graph, start):
    visited = [False] * len(graph)
    distances = [-1] * len(graph)  # Инициализируем расстояния как -1 (недостижимые)
    components = []  # Список для хранения компонент связности

    def bfs_helper(node):
        component = []  # Текущая компонента связности
        queue = deque()
        queue.append(node)
        visited[node] = True
        distances[node] = 0

        while queue:
            current_node = queue.popleft()
            component.append(current_node)

            for neighbor in range(len(graph[current_node])):
                if graph[current_node][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    distances[neighbor] = distances[current_node] + 1

        return component,

    for node in range(len(graph)):
        if not visited[node]:
            components.append(bfs_helper(node))

    return distances, components

# Чтение графа из файла
def read_graph_from_file(filename):
    graph = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = [int(x) for x in line.strip().split()]
            graph.append(row)
    return graph

# Запись результатов в файл
def write_results_to_file(filename, distances, components):
    with open(filename, 'w') as file:
        # Записываем кратчайшие расстояния
        file.write("Кратчайшие расстояния от заданной вершины:\n")
        for i, distance in enumerate(distances):
            file.write(f"Вершина {i}: {distance}\n")

        # Записываем компоненты связности
        file.write("\nКомпоненты связности:\n")
        for i, component in enumerate(components):
            file.write(f"Компонента {i + 1}: {component}\n")

# Задаем имя файла с графом
input_filename = 'input.txt'

# Задаем имя файла для записи результатов
output_filename = 'output.txt'

# Читаем граф из файла
graph = read_graph_from_file(input_filename)

# Начальная вершина
start_vertex = 0

# Выполняем поиск в ширину
distances, components = bfs(graph, start_vertex)

# Записываем результаты в файл
write_results_to_file(output_filename, distances, components)