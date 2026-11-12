import numpy as np

# using numpy

A = np.array([
    [1, 2],
    [3, 4]
])

print(2 * A)

# Ex:

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(A @ B)

print(np.matmul(A, B))