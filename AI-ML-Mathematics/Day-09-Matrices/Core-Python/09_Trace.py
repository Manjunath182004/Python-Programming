A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

trace = 0

for i in range(len(A)):
    trace += A[i][i]

print("Trace:", trace)