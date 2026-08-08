from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
if __name__ == "__main__":

    matrix = Matrix([
        [1, 2],
        [2, 4]
    ])

    print("Nullspace:")
    print(nullspace(matrix))
