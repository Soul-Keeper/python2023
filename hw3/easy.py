import numpy as np

from my_matrix import Matrix


np.random.seed(0)
A = Matrix(np.random.randint(0, 10, (10, 10)))
B = Matrix(np.random.randint(0, 10, (10, 10)))

my_sum = A + B
my_mul = A * B
my_matmul = A @ B

with open('artifacts/easy/matrix+.txt', "wb") as out_file:
    out_file.write(my_sum.__str__().encode())

with open('artifacts/easy/matrix_mul.txt', "wb") as out_file:
    out_file.write(my_mul.__str__().encode())

with open('artifacts/easy/matrix@.txt', "wb") as out_file:
    out_file.write(my_matmul.__str__().encode())
