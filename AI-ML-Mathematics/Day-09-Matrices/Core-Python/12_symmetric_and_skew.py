A = [
    [1, 2],
    [2, 3]
]

transpose = [
    [A[j][i] for j in range(len(A))]
    for i in range(len(A))
]

symmetric = A == transpose

print("Symmetric:", symmetric)