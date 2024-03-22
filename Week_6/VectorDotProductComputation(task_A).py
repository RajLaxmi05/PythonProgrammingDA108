def vector_dot_product(a, b):
    if len(a) != len(b):
        return None
    y = 0
    for i in range(len(a)):
        y += a[i] * b[i]
    return y

a = [1, 2, 3]
b = [4, 5, 6]
result = vector_dot_product(a, b)
print(result)
c = [2, 4, 6, 8]
d = [1, 3, 5]
result = vector_dot_product(c, d)
print(result)
