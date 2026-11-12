import numpy as np

vectors = np.array([
    [1, 0],
    [0, 1]
])

matrix = vectors.T

rank = np.linalg.matrix_rank(matrix)

print("Rank:", rank)
print("Dimension of the span:", rank)

# using standard Basis

# Standard basis of R3
basis = np.eye(3)

print(basis)