u = [4, 1]
v = [1, 3]

# Addition
addition = []

for i in range(len(u)):
    addition.append(u[i] + v[i])

# Subtraction
subtraction = []

for i in range(len(u)):
    subtraction.append(u[i] - v[i])

print("Addition:", addition)
print("Subtraction:", subtraction)


# using numpy

import numpy as np

u = np.array([4, 1])
v = np.array([1, 3])

print("Addition:", u + v)
print("Subtraction:", u - v)

# Three D

import numpy as np

u = np.array([2, 4, 6])
v = np.array([1, 3, 5])

print("u + v:", u + v)
print("u - v:", u - v)