# 8.Реализовать алгоритм Дейкстры поиска кратчайших путей из одной вершины, используя в качестве приоритетной очереди обычный массив


# Функция для чтения графа из файла с матрицей смежности.
def read_graph_from_file(file_name):
    graph = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = [int(x) for x in line.strip().split()]
            graph.append(row)
    return graph


# Функция для нахождения кратчайших путей с помощью алгоритма Дейкстры.
def dijkstra(graph, start_vertex):
    num_vertices = len(graph)
    # Инициализируем массив расстояний с бесконечно большими значениями.
    distances = [float('inf')] * num_vertices
    # Расстояние от начальной вершины до нее самой равно 0.
    distances[start_vertex] = 0
    # Массив для отслеживания посещенных вершин.
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        # Находим вершину с минимальным расстоянием.
        min_distance = float('inf')
        min_vertex = -1
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v

        # Помечаем вершину как посещенную.
        visited[min_vertex] = True

        # Обновляем расстояния до соседних вершин через текущую вершину.
        for v in range(num_vertices):
            if not visited[v] and graph[min_vertex][v] > 0:
                new_distance = distances[min_vertex] + graph[min_vertex][v]
                if new_distance < distances[v]:
                    distances[v] = new_distance

    return distances


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
    shortest_distances = dijkstra(graph, start_vertex)
    write_result_to_file(shortest_distances, output_file)

    print("Результат записан в файл", output_file)