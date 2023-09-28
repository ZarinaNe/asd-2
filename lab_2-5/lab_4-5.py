# Поиск в глубину
# 4.Найти в заданном графе количество и состав компонент связности с помощью поиска в глубину
# 5.Найти в заданном орграфе количество и состав сильно связных компонент с помощью поиска в глубину.


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        # Добавляем ребро между вершинами u и v
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1

    def dfs(self, vertex, visited, component):
        # Рекурсивная функция для обхода в глубину
        visited[vertex] = True
        component.append(vertex)
        for neighbor in range(self.vertices):
            if self.adjacency_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                self.dfs(neighbor, visited, component)

    def find_connected_components(self):
        visited = [False] * self.vertices
        components = []

        for vertex in range(self.vertices):
            if not visited[vertex]:
                component = []
                self.dfs(vertex, visited, component)
                components.append(component)

        return components

    def transpose(self):
        # Транспонирование графа
        transposed = [[0] * self.vertices for _ in range(self.vertices)]
        for i in range(self.vertices):
            for j in range(self.vertices):
                transposed[i][j] = self.adjacency_matrix[j][i]
        return transposed

    def kosaraju(self):
        # Алгоритм Косарайю для поиска сильно связных компонент
        components = []

        # Шаг 1: Обход в глубину для поиска порядка завершения вершин
        visited = [False] * self.vertices
        stack = []

        for vertex in range(self.vertices):
            if not visited[vertex]:
                self.dfs(vertex, visited, stack)

        # Шаг 2: Транспонирование графа
        transposed = self.transpose()

        # Шаг 3: Обратный обход в глубину в порядке, определенном на шаге 1
        visited = [False] * self.vertices

        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                component = []
                self.dfs(vertex, visited, component)
                components.append(component)

        return components


# Чтение графа из файла
def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        vertices = len(lines)
        graph = Graph(vertices)

        for i in range(vertices):
            elements = lines[i].split()
            for j in range(vertices):
                if elements[j] == '1':
                    graph.add_edge(i, j)

        return graph


# Запись результатов в файл
def write_results_to_file(filename, components, description):
    with open(filename, 'w') as file:
        file.write(description + '\n')
        for i, component in enumerate(components):
            file.write(f"Компонента {i + 1}: {component}\n")


# Задаем имя файла с графом
input_filename = 'input.txt'

# Чтение графа из файла
graph = read_graph_from_file(input_filename)

# Поиск компонент связности
connected_components = graph.find_connected_components()

# Запись результатов компонент связности в файл
write_results_to_file('4.txt', connected_components, 'Компоненты связности:')

# Поиск сильно связных компонент
strongly_connected_components = graph.kosaraju()

# Запись результатов сильно связных компонент в файл
write_results_to_file('5.txt', strongly_connected_components, 'Сильно связные компоненты:')