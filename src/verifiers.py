from constants import *

from matrix_engine import *

from parsers import *

# -----------------------------------
# Generic Verifier
# -----------------------------------

def verify_numeric(question, solver):

    matrix = extract_matrix(question)

    expected = extract_answer(question)

    if expected is None:
        return False

    computed = solver(matrix)

    expected = float(expected)

    return abs(float(computed) - expected) < 1e-6

