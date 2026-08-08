from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
matrix = Matrix([
    [2, 0],
    [0, 3]

    [2, 1],
    [0, 2]
])

print("Eigenvalues:")
print(eigenvalues(matrix))
