# 9. Реализовать алгоритм Беллмана-Форда поиска кратчайших путей из одной вершины

# Функция для чтения графа из файла с матрицей смежности.
def read_graph_from_file(file_name):
    graph = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = [int(x) for x in line.strip().split()]
            graph.append(row)
    return graph

# Функция для нахождения кратчайших путей с помощью алгоритма Беллмана-Форда.
def bellman_ford(graph, start_vertex):
    num_vertices = len(graph)
    # Инициализируем массив расстояний с бесконечно большими значениями.
    distances = [float('inf')] * num_vertices
    # Расстояние от начальной вершины до нее самой равно 0.
    distances[start_vertex] = 0

    # Проходим по всем вершинам (n-1) раз, где n - количество вершин в графе.
    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v in range(num_vertices):
                if graph[u][v] != 0:
                    new_distance = distances[u] + graph[u][v]
                    if new_distance < distances[v]:
                        distances[v] = new_distance

    # Дополнительная итерация для обнаружения цикла отрицательного веса.
    for u in range(num_vertices):
        for v in range(num_vertices):
            if graph[u][v] != 0:
                new_distance = distances[u] + graph[u][v]
                if new_distance < distances[v]:
                    # Обнаружен отрицательный цикл в графе
                    return None

    return distances  # Возвращаем список расстояний

# Функция для записи результата в файл.
def write_result_to_file(result, output_file):
    with open(output_file, 'w') as file:
        for i, distance in enumerate(result):
            file.write(f"Shortest distance from vertex 0 to vertex {i}: {distance}\n")

# Основная часть программы.
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    start_vertex = 0  # Начальная вершина для поиска кратчайших путей.

    graph = read_graph_from_file(input_file)
    has_negative_cycle = bellman_ford(graph, start_vertex)

if has_negative_cycle is None:
    print("Граф содержит отрицательный цикл.")
else:
    shortest_distances = bellman_ford(graph, start_vertex)
    if shortest_distances is not None:
        write_result_to_file(shortest_distances, output_file)
        print("Результат записан в файл", output_file)
    else:
        print("Граф содержит отрицательный цикл, результат не может быть вычислен.")