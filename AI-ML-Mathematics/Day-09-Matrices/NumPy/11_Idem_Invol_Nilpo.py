import numpy as np

# Idempotent matrix: A @ A = A
A = np.array([
    [1, 0],
    [0, 0]
])

print("Idempotent:", np.allclose(A @ A, A))


# Involutory matrix: A @ A = I
B = np.array([
    [0, 1],
    [1, 0]
])

print("Involutory:", np.allclose(B @ B, np.eye(2)))


# Nilpotent matrix: some positive power becomes zero
C = np.array([
    [0, 1],
    [0, 0]
])

print("Nilpotent:", np.allclose(C @ C, np.zeros((2, 2))))