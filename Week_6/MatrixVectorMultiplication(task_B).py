def matrix_vector_multiply(matrix, vector):
    num_cols = len(matrix[0])
    if num_cols != len(vector):
        raise ValueError("Alert: Col count in matrix not matching length of vector")
    result = [0] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result
    
matrix = [[1, 2], [3, 4]]
vector = [5, 6]
result = matrix_vector_multiply(matrix, vector)   
print(result)
try:
    result = matrix_vector_multiply(matrix, vector)
except ValueError as e:
    print(e)    
