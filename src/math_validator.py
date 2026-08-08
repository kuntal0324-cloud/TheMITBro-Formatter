from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
if __name__ == "__main__":

    matrix = Matrix([
        [2, 0],
        [0, 3]
    ])

    result = eigenvalues(matrix)

    print("Raw:", result)
    print("Expanded:", expand_eigenvalues(result))
