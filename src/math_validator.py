from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------

matrix = [
    [2, 0],
    [0, 3]
]

P, D = diagonalize_matrix(matrix)

print("P:")
print(P)

print("D:")
print(D)

print("Reconstructed:")
print(P * D * P.inv())

print("Original:")
print(Matrix(matrix))

print("Verify:", P * D * P.inv() == Matrix(matrix))
