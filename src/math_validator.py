from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
from sympy import Matrix

if __name__ == "__main__":

    matrix = Matrix([
        [1, 2],
        [2, 4]
    ])

    print("RREF:")
    print(rref(matrix))
