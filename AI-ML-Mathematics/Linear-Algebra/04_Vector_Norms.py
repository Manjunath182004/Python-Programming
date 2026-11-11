
import math

vector = [3, 4]

#L1 Norm
l1_norm = sum(abs(x) for x in vector)

# L2 norm

l2_norm = math.sqrt(sum(x**2 for x in vector))

print("L1 norm:", l1_norm)
print("L2 norm:", l2_norm)


# in numpy

import numpy as np

vector = np.array([3, 4])

l1_norm = np.linalg.norm(vector, ord=1)
l2_norm = np.linalg.norm(vector, ord=2)

print("L1 norm:", l1_norm)
print("L2 norm:", l2_norm)

# Ex:

vectors = [
    np.array([3, 4]),
    np.array([1, 2, 3]),
    np.array([-3, 4]),
    np.array([5, -2, 7])
]

for vector in vectors:
    print("\nVector:", vector)
    print("L1:", np.linalg.norm(vector, ord=1))
    print("L2:", np.linalg.norm(vector, ord=2))