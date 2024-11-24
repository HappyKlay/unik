import numpy as np

# Исходная матрица
matrix = np.array([
    [1, 1/3, 3],
    [3, 1, 2],
    [1/3, 1/2, 1]
])



# Размерность матрицы
n = 3

# Нормализуем матрицу
column_sums = np.sum(matrix, axis=0)
normalized_matrix = matrix / column_sums

# Рассчитываем вектор весов
weights = np.mean(normalized_matrix, axis=1)

# Рассчитываем λmax
lambda_max_vector = np.dot(matrix, weights) / weights
lambda_max = np.mean(lambda_max_vector)

# Рассчитываем индекс согласованности
Iy = (lambda_max - n) / (n - 1)
Iy

M_Iy = 0

if n == 3:
    M_Iy = 0.58


Io = Iy / M_Iy

print(Io)