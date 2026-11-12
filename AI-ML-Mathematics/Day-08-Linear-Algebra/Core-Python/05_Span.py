v1 = [1, 0]
v2 = [0, 1]

coefficients = [
    (1,1), (2, 3), (-1, 4), (5, -2)
]


for a, b in coefficients:
    result = []
    for i in range(2):
        result.append(a * v1[i] + b * v2[i])

    print(result)