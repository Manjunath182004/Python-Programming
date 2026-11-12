A = [
    [2, 1],
    [1, 1]
]

a, b = A[0]
c, d = A[1]

det = a * d - b * c

if det != 0:
    inverse = [
        [d / det, -b / det],
        [-c / det, a / det]
    ]

    print(inverse)
else:
    print("Inverse does not exist")