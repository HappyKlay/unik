import numpy as np

# Исходная матрица
matrix = np.array([
    [1, 2, 8],
    [1/2, 1, 9],
    [1/8, 1/9, 1]
])

# Нормализуем матрицу
column_sums = np.sum(matrix, axis=0)
normalized_matrix = matrix / column_sums

# Рассчитываем вектор весов
weights = np.mean(normalized_matrix, axis=1)

# Рассчитываем λmax
lambda_max_vector = np.dot(matrix, weights) / weights
lambda_max = np.mean(lambda_max_vector)

normalized_matrix, weights, lambda_max

print(normalized_matrix)
print(weights)
print(lambda_max)
