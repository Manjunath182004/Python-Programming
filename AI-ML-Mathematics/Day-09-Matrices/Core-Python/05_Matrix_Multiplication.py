A = [
    [1, 2],
    [3, 4]
]

k = 2

result = [
    [k * value for value in row]
    for row in A
]

print(result)


# Ex:

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

rows_A = len(A)
cols_A = len(A[0])
cols_B = len(B[0])

result = [
    [0 for j in range(cols_B)]
    for i in range(rows_A)
]

for i in range(rows_A):
    for j in range(cols_B):
        for k in range(cols_A):
            result[i][j] += A[i][k] * B[k][j]

print(result)