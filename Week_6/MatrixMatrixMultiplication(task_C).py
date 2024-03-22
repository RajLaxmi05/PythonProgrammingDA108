def matrix_multiply(matrix1, matrix2):
    num_cols_matrix1 = len(matrix1[0])
    num_rows_matrix2 = len(matrix2)
    if num_cols_matrix1 != num_rows_matrix2:
        raise ValueError("Incompatible dimensions for matrix multiplication")
    result = [[0] * len(matrix2[0]) for i in range (len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = matrix_multiply(matrix1, matrix2)
print(result) 

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
result = matrix_multiply(matrix1, matrix2)
print(result) 

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6, 7], [8, 9, 10]]
result = matrix_multiply(matrix1, matrix2)
print(result) 
try:
    result = matrix_multiply(matrix1, matrix2)
except ValueError as e:
    print(e) 
