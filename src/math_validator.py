from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
if __name__ == "__main__":

    from sympy import sqrt, Rational, pi

    tests = [

        ("Exact",
         [[1, 2], [3, 4]],
         [[1, 2], [3, 4]]),

        ("Decimal vs Fraction",
         [[Rational(1, 2), 2]],
         [[0.5, 2]]),

        ("Symbolic",
         [[sqrt(2) * sqrt(2), pi]],
         [[2, pi]]),

        ("Different",
         [[1, 2]],
         [[1, 3]]),
    ]

    for name, computed, expected in tests:

        result = compare_matrices(
            Matrix(computed),
            expected
        )

        print(name, ":", result)
