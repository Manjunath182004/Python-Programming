basis = [
    [1, 0],
    [0, 1]
]

dimension = len(basis)

print("Basis:", basis)
print("Dimension:", dimension)

# For Standarad Basis

a = 4
b = 5

e1 = [1, 0]
e2 = [0, 1]

result = [
    a * e1[i] + b * e2[i]
    for i in range(2)
]

print(result)

# For standard basis R^3

e1 = [1, 0, 0]
e2 = [0, 1, 0]
e3 = [0, 0, 1]

a, b, c = 4, 5, 6

result = [
    a * e1[i] + b * e2[i] + c * e3[i]
    for i in range(3)
]

print("Vector:", result)