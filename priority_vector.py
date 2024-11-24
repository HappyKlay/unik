import numpy as np

# Матрица предпочтений из таблицы
A = np.array([
    [1, 2, 8],
    [1/2, 1, 9],
    [1/8, 1/9, 1] 
], dtype=float)

# Нормализуем матрицу по столбцам
normalized_matrix = A / A.sum(axis=0)

# Вычисляем вектор приоритетов как среднее значение строк
priority_vector = normalized_matrix.mean(axis=1)

priority_vector

print(priority_vector)