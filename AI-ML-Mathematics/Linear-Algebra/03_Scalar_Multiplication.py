vector = [1, 2]
scalar = 3

result = []

for value in vector:
    result.append(scalar * value)

print("Original vector:", vector)
print("Scalar:", scalar)
print("Result:", result)

# in numpy

import numpy as np

vector = np.array([1, 2])
scalar = 3

result = scalar * vector

print("Original vector:", vector)
print("Result:", result)


# negativce ex 

vector = np.array([2, 4])

print("Original:", vector)
print("Multiply by 2:", 2 * vector)
print("Multiply by -1:", -1 * vector)
print("Multiply by -2:", -2 * vector)