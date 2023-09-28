# 7.Реализовать алгоритм Прима нахождения минимального покрывающего дерева.

# Функция для чтения графа из файла с матрицей смежности.
def read_graph_from_file(file_name):
    graph = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = [int(x) for x in line.strip().split()]
            graph.append(row)
    return graph


# Функция для нахождения минимального покрывающего дерева с помощью алгоритма Прима.
def prim(graph):
    num_vertices = len(graph)
    # Инициализируем список вершин и ребер, начиная с первой вершины.
    vertices = [0]
    edges = []

    # Пока не добавим все вершины в список вершин:
    while len(vertices) < num_vertices:
        min_edge = None
        min_weight = float('inf')

        # Ищем ребро с минимальным весом, которое соединяет вершину из списка с вершиной не в списке.
        for vertex in vertices:
            for neighbor in range(num_vertices):
                if neighbor not in vertices and graph[vertex][neighbor] != 0:
                    weight = graph[vertex][neighbor]
                    if weight < min_weight:
                        min_weight = weight
                        min_edge = (vertex, neighbor, weight)

        # Добавляем вершину и ребро в списки.
        vertices.append(min_edge[1])
        edges.append(min_edge)

    return edges


# Функция для записи результата в файл.
def write_result_to_file(result, output_file):
    with open(output_file, 'w') as file:
        for edge in result:
            file.write(f"{edge[0]} - {edge[1]} (Weight: {edge[2]})\n")


# Основная часть программы.
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    graph = read_graph_from_file(input_file)
    minimum_spanning_tree = prim(graph)
    write_result_to_file(minimum_spanning_tree, output_file)

    print("Минимальное покрывающее дерево записано в файл", output_file)