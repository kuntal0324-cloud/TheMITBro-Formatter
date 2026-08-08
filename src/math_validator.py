from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------

if __name__ == "__main__":

    matrix = [
        [2, 0],
        [0, 2]
    ]

    result = eigenvectors(matrix)

    print("Eigenvectors:", result)
