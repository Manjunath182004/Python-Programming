import numpy as np

A = np.array([
    [2, 1],
    [1, 1]
])

inverse = np.linalg.inv(A)

print(inverse)