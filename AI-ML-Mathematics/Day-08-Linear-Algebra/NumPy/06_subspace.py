import numpy as np

# Vectors belonging to the x-axis subset
v1 = np.array([2, 0])
v2 = np.array([3, 0])

# Zero vector
zero = np.array([0, 0])

# Addition
addition = v1 + v2

# Scalar multiplication
multiplication = 3 * v1

print("Zero:", zero)
print("Addition:", addition)
print("Scalar multiplication:", multiplication)

print("Addition remains on x-axis:", addition[1] == 0)
print("Scalar result remains on x-axis:", multiplication[1] == 0)