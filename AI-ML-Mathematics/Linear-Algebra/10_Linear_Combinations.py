v1 = [1, 0]
v2 = [1, 2]

c1 = 3
c2 = 2

result = []

for i in range(len(v1)):
    value = c1 * v1[i] + c2 * v2[i]
    result.append(value)

print("Linear combination:", result)


# Using Numpy

import numpy as np

v1 = np.array([1, 0])
v2 = np.array([1, 2])

c1 = 3
c2 = 2

result = c1 * v1 + c2 * v2

print("Linear combination:", result)

# Three Vector Ex:

import numpy as np

v1 = np.array([1, 0, 0])
v2 = np.array([1, 2, 1])
v3 = np.array([2, 3, 1])

result = 1 * v1 + 4 * v2 - 2 * v3

print("Result:", result)


# Resuable function 


def linear_combination(vectors, coefficients):
    if len(vectors) != len(coefficients):
        raise ValueError("Number of vectors and coefficients must match")

    if not vectors:
        return []

    dimension = len(vectors[0])

    if any(len(v) != dimension for v in vectors):
        raise ValueError("All vectors must have the same dimension")

    result = [0] * dimension

    for vector, coefficient in zip(vectors, coefficients):
        for i in range(dimension):
            result[i] += coefficient * vector[i]

    return result


vectors = [
    [1, 0],
    [1, 2],
    [2, 3]
]

coefficients = [1, 4, -2]

print(linear_combination(vectors, coefficients))