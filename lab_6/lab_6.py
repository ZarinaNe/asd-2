# 6.Минимальные покрывающие деревья
# Реализовать алгоритм Крускала нахождения минимального покрывающего дерева.

# Создаем класс для представления ребра графа.
class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

# Функция для чтения графа из файла с матрицей смежности.
def read_graph_from_file(file_name):
    graph = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = [int(x) for x in line.strip().split()]
            graph.append(row)
    return graph

# Функция для нахождения минимального покрывающего дерева с помощью алгоритма Крускала.
def kruskal(graph):
    num_vertices = len(graph)
    edges = []

    # Создаем список всех ребер с их весами.
    for i in range(num_vertices):
        for j in range(i, num_vertices):
            if graph[i][j] != 0:
                edges.append(Edge(i, j, graph[i][j]))

    # Сортируем ребра по весу.
    edges.sort(key=lambda edge: edge.weight)

    # Инициализируем структуры данных для отслеживания компонентов связности.
    parent = [i for i in range(num_vertices)]
    minimum_spanning_tree = []

    # Функция для поиска корня компонента связности.
    def find_root(vertex):
        if parent[vertex] == vertex:
            return vertex
        return find_root(parent[vertex])

    # Объединяем компоненты связности, пока не построим минимальное покрывающее дерево.
    for edge in edges:
        root_start = find_root(edge.start)
        root_end = find_root(edge.end)

        if root_start != root_end:
            minimum_spanning_tree.append(edge)
            parent[root_start] = root_end

    return minimum_spanning_tree

# Функция для записи результата в файл.
def write_result_to_file(result, output_file):
    with open(output_file, 'w') as file:
        for edge in result:
            file.write(f"{edge.start} - {edge.end} (Weight: {edge.weight})\n")

# Основная часть программы.
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    graph = read_graph_from_file(input_file)
    minimum_spanning_tree = kruskal(graph)
    write_result_to_file(minimum_spanning_tree, output_file)

    print("Минимальное покрывающее дерево записано в файл", output_file)