# 10.Реализовать алгоритм нахождения эйлерова цикла в неориентированном графе, заданном матрицей смежности.

# Функция для чтения графа из файла с матрицей смежности.
def read_graph_from_file(file_name):
    graph = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = [int(x) for x in line.strip().split()]
            graph.append(row)
    return graph

# Функция для нахождения Эйлерова цикла.
def find_eulerian_cycle(graph):
    num_vertices = len(graph)
    # Создаем копию графа для модификации.
    modified_graph = [row[:] for row in graph]

    # Список для хранения вершин пути.
    eulerian_path = []
    # Начинаем с произвольной вершины (в данном примере с 0).
    current_vertex = 0
    eulerian_path.append(current_vertex)

    while True:
        # Ищем непосещенного соседа текущей вершины.
        for neighbor in range(num_vertices):
            if modified_graph[current_vertex][neighbor] == 1:
                # Удаляем ребро между текущей вершиной и соседом.
                modified_graph[current_vertex][neighbor] = 0
                modified_graph[neighbor][current_vertex] = 0
                # Переходим к соседу.
                current_vertex = neighbor
                eulerian_path.append(current_vertex)
                break
        else:
            # Если все соседи уже посещены, завершаем цикл.
            break

    return eulerian_path

# Функция для записи результата в файл.
def write_result_to_file(result, output_file):
    with open(output_file, 'w') as file:
        file.write("Eulerian Cycle: ")
        file.write(" -> ".join(map(str, result)))

# Основная часть программы.
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    graph = read_graph_from_file(input_file)
    eulerian_cycle = find_eulerian_cycle(graph)
    write_result_to_file(eulerian_cycle, output_file)

    print("Результат записан в файл", output_file)