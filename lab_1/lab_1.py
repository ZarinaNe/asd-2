# 1.Нахождение выпуклой оболочки множества точек
# В данной задаче требуется ввести N точек своими координатами (x,y). Затем требуется определить, существует ли выпуклая оболочка
# заданного множества точек.
# алгоритм Грэхема.

# Алгоритм Грэхема - это один из методов нахождения выпуклой оболочки множества точек в двумерном пространстве. Этот алгоритм
# работает за время O(n * log(n)), где n - количество точек. Этот код сначала находит точку с минимальной y-координатой и
# сортирует остальные точки по углу относительно этой точки. Затем он использует стек для построения выпуклой оболочки, начиная
# с первых двух отсортированных точек. В результате работы алгоритма выпуклая оболочка будет храниться в списке hull.


# Импортируем библиотеку для сортировки точек
from functools import cmp_to_key


# Функция для определения ориентации трех точек (p, q, r).
# Возвращает 0, если точки коллинеарны, положительное значение, если поворот по часовой стрелке,
# и отрицательное значение, если поворот против часовой стрелки.
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1


# Функция для сравнения двух точек. Используется при сортировке.
# Сравнивает точки по углу, который они образуют относительно начальной точки p.
def compare(p, q):
    # Вычисляем ориентацию точек относительно начальной точки p.
    # Если ориентации одинаковы, сравниваем точки по расстоянию до p.
    o = orientation(p, p, q)
    if o == 0:
        return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
    return o


# Основная функция для нахождения выпуклой оболочки.
def convex_hull(points):
    n = len(points)

    # Находим точку с минимальной y-координатой (и самой левой, если есть несколько таких точек).
    start = min(points, key=lambda point: (point[1], point[0]))

    # Сортируем остальные точки на основе их углов относительно начальной точки.
    sorted_points = sorted(points,
                           key=cmp_to_key(lambda point1, point2: compare(start, point1) - compare(start, point2)))

    # Инициализируем стек для построения оболочки.
    hull = [sorted_points[0], sorted_points[1]]

    # Построение оболочки.
    for i in range(2, n):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i]) != -1:
            hull.pop()
        hull.append(sorted_points[i])

    return hull


# Ввод N точек
N = int(input("Введите количество точек: "))
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# Находим выпуклую оболочку
hull = convex_hull(points)

# Выводим результат
print("Выпуклая оболочка:")
for point in hull:
    print(point)