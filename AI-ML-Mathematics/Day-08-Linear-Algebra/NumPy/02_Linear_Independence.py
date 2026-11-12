import numpy as np

v1 = np.array([1, 2])
v2 = np.array([3, 1])

a = 2
b = 3

result = a * v1 + b * v2

print(result)


# Using Matrix

v1 = np.array([1, 2])
v2 = np.array([2, 4])

matrix = np.column_stack((v1, v2))

rank = np.linalg.matrix_rank(matrix)

print("Matrix:\n", matrix)
print("Rank:", rank)

if rank == 2:
    print("Linearly Independent")
else:
    print("Linearly Dependent")

# Ex:

v1 = np.array([1, 0])
v2 = np.array([0, 1])

matrix = np.column_stack((v1, v2))

print("Rank:", np.linalg.matrix_rank(matrix))    