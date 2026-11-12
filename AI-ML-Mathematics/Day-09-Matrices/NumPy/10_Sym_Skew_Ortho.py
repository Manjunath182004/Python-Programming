import numpy as np

A = np.array([
    [1, 2],
    [2, 3]
])

# Symmetric
print("Symmetric:", np.allclose(A.T, A))

# Skew-symmetric
B = np.array([
    [0, 2],
    [-2, 0]
])

print("Skew-symmetric:", np.allclose(B.T, -B))

# Orthogonal
Q = np.array([
    [0, 1],
    [1, 0]
])

print("Orthogonal:", np.allclose(Q.T @ Q, np.eye(2)))