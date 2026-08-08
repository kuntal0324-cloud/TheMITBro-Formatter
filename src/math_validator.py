from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
from sympy import Matrix

if __name__ == "__main__":

    computed = Matrix([
        [1, 2],
        [5, 4]
    ])

    expected = [
        [1, 2],
        [3, 4]
    ]

    result = matrix_comparison_details(
        computed,
        expected
    )

    print(result)
