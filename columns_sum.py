import numpy as np

# Матрица предпочтений из таблицы
A = np.array([
    [1, 2, 8],
    [1/2, 1, 9],
    [1/8, 1/9, 1]
], dtype=float)

# Сумма элементов каждого столбца матрицы A
column_sums = A.sum(axis=0)
column_sums
print(column_sums)
