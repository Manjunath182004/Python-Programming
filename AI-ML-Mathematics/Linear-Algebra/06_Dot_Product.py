quantity = [3, 5, 2]
price = [10, 20, 30]

total_cost = 0

for i in range(len(quantity)):
    total_cost += quantity[i] * price[i]

print("Total purchase cost:", total_cost)

# using numpy

import numpy as np

quantity = np.array([3, 5, 2])
price = np.array([10, 20, 30])

total_cost = np.dot(quantity, price)

print("Total purchase cost:", total_cost)


# Examples:


u = np.array([2, 3])
v = np.array([4, 5])

print("Example 1:", np.dot(u, v))

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

print("Example 2:", np.dot(u, v))

u = np.array([2, 0, 1])
v = np.array([3, 4, 5])

print("Example 3:", np.dot(u, v))


# Implement dot product without NumPy

def dot_product(u, v):
    if len(u) != len(v):
        raise ValueError("Vectors must have equal dimensions")

    result = 0

    for i in range(len(u)):
        result += u[i] * v[i]

    return result

print(dot_product([3, 5, 2], [10, 20, 30]))
print(dot_product([2, 3], [4, 5]))