# 16.Задача о рюкзаке
# В этой задаче у нас есть набор предметов, каждый из которых имеет свой вес и стоимость, и мы должны выбрать подмножество
# предметов так, чтобы их суммарный вес не превышал вместимость рюкзака, а суммарная стоимость была максимальной.


# Заданные предметы: каждый элемент - кортеж (вес, стоимость)
items = [(2, 6), (2, 10), (3, 12), (4, 13)]

# Вместимость рюкзака
capacity = 5

# Функция для решения задачи о рюкзаке
def knapsack(items, capacity):
    n = len(items)
    # Создаем двумерную таблицу для хранения максимальных стоимостей
    # dp[i][w] будет содержать максимальную стоимость для первых i предметов
    # при ограниченной вместимости w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Заполняем таблицу построчно
    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            # Если вес текущего предмета больше оставшейся вместимости, мы не можем его взять
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Мы выбираем максимум из двух вариантов:
                # 1. Взять текущий предмет и добавить его стоимость к стоимости предыдущих предметов
                # 2. Не брать текущий предмет и оставить стоимость как у предыдущих предметов
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    # Теперь нужно восстановить выбранные предметы
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            weight, value = items[i - 1]
            selected_items.append((weight, value))
            w -= weight

    return dp[n][capacity], selected_items

# Решаем задачу о рюкзаке
max_value, selected_items = knapsack(items, capacity)

# Выводим результат
print(f"Максимальная стоимость: {max_value}")
print("Выбранные предметы:")
for item in selected_items:
    print(f"Вес: {item[0]}, Стоимость: {item[1]}")