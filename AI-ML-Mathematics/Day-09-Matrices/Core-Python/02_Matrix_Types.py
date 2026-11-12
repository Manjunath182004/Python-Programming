def matrix_type(A):
    rows = len(A)
    cols = len(A[0])

    if rows == 1:
        return "Row Matrix"
    elif cols == 1:
        return "Column Matrix"
    elif rows == cols:
        return "Square Matrix"
    else:
        return "Rectangular Matrix"


A = [[1, 2, 3], [4, 5, 6]]
print(matrix_type(A))