# Задача о раскладке по ящикам (Bin Packing Problem) - это комбинаторная задача оптимизации, в которой нужно упаковать объекты в
# ящики с минимальным количеством ящиков. Решение этой задачи с помощью жадного алгоритма:

# Заданные объекты, каждый из которых имеет свой размер
objects = [4, 8, 1, 2, 6, 7]
# Вместимость одного ящика
bin_capacity = 10

# Функция для раскладки объектов по ящикам
def bin_packing(objects, bin_capacity):
    bins = []  # Список, в котором будут храниться ящики и их содержимое

    # Проходимся по каждому объекту и пытаемся упаковать его в существующие ящики
    for obj in objects:
        packed = False

        # Проходимся по существующим ящикам и пытаемся упаковать объект
        for i, bin in enumerate(bins):
            if sum(bin) + obj <= bin_capacity:
                bin.append(obj)  # Добавляем объект в текущий ящик
                packed = True
                break

        # Если не удалось упаковать объект в существующие ящики, создаем новый ящик
        if not packed:
            new_bin = [obj]
            bins.append(new_bin)

    return bins

# Раскладываем объекты по ящикам
packed_bins = bin_packing(objects, bin_capacity)

# Выводим результат
print("Раскладка по ящикам:")
for i, bin in enumerate(packed_bins):
    print(f"Ящик {i + 1}: {bin}")