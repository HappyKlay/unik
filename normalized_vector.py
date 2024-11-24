import numpy as np

# Матрица предпочтений из таблицы
A = np.array([
    [1, 2, 8],
    [1/2, 1, 9],
    [1/8, 1/9, 1]
], dtype=float)

# Собственные значения и собственные векторы
eigenvalues, eigenvectors = np.linalg.eig(A)

# Находим главный собственный вектор (связанный с максимальным собственным значением)
max_index = np.argmax(eigenvalues.real)
principal_eigenvector = eigenvectors[:, max_index].real

# Нормализация собственного вектора
normalized_vector = principal_eigenvector / principal_eigenvector.sum()

normalized_vector

print(normalized_vector)