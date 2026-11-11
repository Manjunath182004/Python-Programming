def check_linear_independence_2d(v1, v2):

    determinant = v1[0] * v2[1] - v1[1] * v2[0]

    if determinant == 0:
        print("Linearly Dependent")
    else:
        print("Linearly Independent")


check_linear_independence_2d([1, 2], [2, 4])

check_linear_independence_2d([1, 0], [0, 1])

check_linear_independence_2d([2, 3], [4, 5])


# Using Numpy

import numpy as np

# Dependent vectors
v1 = [1, 2]
v2 = [2, 4]

A = np.column_stack((v1, v2))

rank = np.linalg.matrix_rank(A)

if rank == A.shape[1]:
    print("Linearly Independent")
else:
    print("Linearly Dependent")


# Ex:

import numpy as np

v1 = [1, 0]
v2 = [0, 1]

A = np.column_stack((v1, v2))

print("Matrix:\n", A)
print("Rank:", np.linalg.matrix_rank(A))
print("Number of vectors:", A.shape[1])


# Ex:

import numpy as np

examples = [
    [[1, 2], [2, 4]],
    [[1, 0], [0, 1]],
    [[1, 2], [3, 6]],
    [[2, 3], [4, 5]]
]

for vectors in examples:

    matrix = np.column_stack(vectors)

    rank = np.linalg.matrix_rank(matrix)

    if rank == len(vectors):
        result = "Independent"
    else:
        result = "Dependent"

    print(vectors, "=>", result)
