# 16.Задача о рюкзаке
# В этой задаче у нас есть набор предметов, каждый из которых имеет свой вес и стоимость, и мы должны выбрать подмножество
# предметов так, чтобы их суммарный вес не превышал вместимость рюкзака, а суммарная стоимость была максимальной.


def knapsack_dynamic(w, p, n, max_weight):
    # Создаем таблицу A для хранения промежуточных результатов размером (n+1) x (max_weight+1)
    A = [[0] * (max_weight + 1) for _ in range(n + 1)]

    # Заполняем таблицу A
    for i in range(n + 1):
        for s in range(max_weight + 1):
            if i == 0 or s == 0:
                # Начальные условия: нулевая строка и нулевой столбец равны нулю
                A[i][s] = 0
            elif s >= w[i - 1]:
                # Если текущий предмет вмещается в рюкзак
                A[i][s] = max(A[i - 1][s], A[i - 1][s - w[i - 1]] + p[i - 1])
            else:
                # Если текущий предмет не вмещается в рюкзак
                A[i][s] = A[i - 1][s]

    return A

def find_ans(A, w, n, max_weight):
    ans = []
    k, s = n, max_weight

    while k > 0 and s > 0:
        if A[k][s] != A[k - 1][s]:
            # Если текущий предмет входит в оптимальное решение
            ans.append(k)
            s -= w[k - 1]
        k -= 1

    return ans

# Пример использования
weights = [2, 3, 4, 5]  # Веса предметов
profits = [3, 4, 5, 6]  # Прибыль от предметов
num_items = len(weights)  # Количество предметов
max_weight = 5          # Максимальный вес рюкзака

A = knapsack_dynamic(weights, profits, num_items, max_weight)
selected_items = find_ans(A, weights, num_items, max_weight)

print("Максимальная прибыль:", A[num_items][max_weight])
print("Выбранные предметы:", selected_items)