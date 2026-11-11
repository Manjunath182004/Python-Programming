"""
orthogonal vectors
Two vectors are said to be orthogonal when their dot product is zero

"""

# Ex

def check_orthogonal(u, v):

    dot = sum(u[i] * v[i] for i in range(len(u)))

    if dot == 0:
        print("vectors are orthogonal")
    else:
        print("vectors are not orthogonal")

check_orthogonal([-1, 3], [6, 2])
check_orthogonal([1, 2], [3, 4])


# using Numpy

import numpy as np

u = np.array([-1, 3])
v = np.array([6, 2])

dot = np.dot(u, v)

print("Dot product:", dot)
print("Orthogonal:", np.isclose(dot, 0))    # np.isclose() is useful because floating-point calculations can produce tiny errors instead of an exact zero.

# Ex2 

u = np.array([1, 0])
v = np.array([0, 1])

dot = np.dot(u, v)

print("Dot product:", dot)
print("Orthogonal:", np.isclose(dot, 0)) 

# Ex3

u = np.array([1, 2])
v = np.array([4, 5])

dot = np.dot(u, v)

print("Dot product:", dot)
print("Orthogonal:", np.isclose(dot, 0))

# ex4

u = np.array([1, 2, 3])
v = np.array([2, -1, 0])

dot = np.dot(u, v)

print("Dot product:", dot)
print("Orthogonal:", np.isclose(dot, 0))