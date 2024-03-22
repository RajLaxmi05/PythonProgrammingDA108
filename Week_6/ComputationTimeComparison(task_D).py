import time
import numpy as np

def matrix_vector_product(matrix, vector):
    result = []
    for row in matrix:
        result.append(sum(row[i]*vector[i] for i in range(len(vector))))
    return result

matrix_size = 1000
vector_size = 1000

# create a matrix with elements chosen randomly from 1-9
matrix = [[np.random.randint(1, 10) for i in range(vector_size)] for i in range(matrix_size)]
# create a vector with elements chosen randomly from 1-9
vector = [np.random.randint(1, 10) for i in range(vector_size)]


start_time = time.time()
result_list = matrix_vector_product(matrix, vector)
end_time = time.time()
list_time = end_time - start_time
print(f"List implementation time: {list_time:.6f} seconds")

start_time = time.time()
matrix_np = np.array(matrix)
vector_np = np.array(vector)
result_np = np.dot(matrix_np, vector_np)
end_time = time.time()
numpy_time = end_time - start_time
print(f"NumPy implementation time: {numpy_time:.6f} seconds")


assert np.array_equal(result_list, result_np)
print("Results are the same")