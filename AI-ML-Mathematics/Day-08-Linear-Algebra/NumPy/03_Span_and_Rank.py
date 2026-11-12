import numpy as np

v1 = np.array([1, 0])
v2 = np.array([0, 1])

a = 4
b = 5

result = a * v1 + b * v2

print("Linear Combination:", result)

# check wether vector belongs to span

A = np.array([
    [1, 0],
    [0, 1]
])

w = np.array([4, 5])

coefficients = np.linalg.solve(A, w)

print("Coefficients:", coefficients)
print("Reconstructed vector:", A @ coefficients)