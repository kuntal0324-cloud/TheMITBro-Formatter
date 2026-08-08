from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------

matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [1, 1, 1]
]

computed_rank = matrix_rank(matrix)

print("Rank:", computed_rank)
