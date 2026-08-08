from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------

matrix = [
    [4, 7],
    [2, 6]
]

A = Matrix(matrix)
A_inv = inverse_matrix(matrix)

print("Inverse:")
print(A_inv)

print("A * A_inv:")
print(A * A_inv)

print("Verify:", A * A_inv == Matrix.eye(A.rows))
