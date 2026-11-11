matrix = [
    [5, 2, 3, 6],
    [2, 5, 3, 6],
    [1, 2, 3, 2]
]

print("Matrix:")

for row in matrix:
    print(row)

print("Number of rows:", len(matrix))
print("Number of columns:", len(matrix[0]))

# Access an element
print("Element at row 1, column 2:", matrix[0][1])

# First row
print("First row:", matrix[0])

# First column
first_column = [row[0] for row in matrix]
print("First column:", first_column)


# using Numpy

import numpy as np

A = np.array([
    [5, 2, 3, 6],
    [2, 5, 3, 6],
    [1, 2, 3, 2]
])

print("Matrix:\n", A)

print("Shape:", A.shape)
print("Rows:", A.shape[0])
print("Columns:", A.shape[1])

print("First row:", A[0])
print("First column:", A[:, 0])
print("Element at row 1, column 2:", A[0, 1])