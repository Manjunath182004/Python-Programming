import numpy as np

# Row matrix
row = np.array([[1, 2, 3]])

# Column matrix
column = np.array([[1], [2], [3]])

# Square matrix
square = np.array([[1, 2], [3, 4]])

# Rectangular matrix
rectangular = np.array([[1, 2, 3], [4, 5, 6]])

# Zero matrix
zero = np.zeros((3, 3))

# Identity matrix
identity = np.eye(3)

# Diagonal matrix
diagonal = np.diag([2, 4, 6])

print("Identity Matrix:\n", identity)
print("Diagonal Matrix:\n", diagonal)