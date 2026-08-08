from sympy import simplify

from constants import *

from matrix_engine import *

from parsers import *

# -----------------------------------
# Generic Verifier
# -----------------------------------

def compare_matrices(computed, expected):

    if computed.shape != (len(expected), len(expected[0])):
        return False

    for i in range(computed.rows):
        for j in range(computed.cols):

            difference = simplify(
                computed[i, j] - expected[i][j]
            )

            if difference != 0:
                return False

    return True

def compare_matrix_lists(computed, expected):

    if len(computed) != len(expected):
        return False

    for computed_matrix, expected_matrix in zip(
        computed,
        expected
    ):

        if not compare_matrices(
            Matrix(computed_matrix),
            expected_matrix
        ):
            return False

    return True

def matrix_comparison_details(computed, expected):

    if computed.shape != (len(expected), len(expected[0])):
        return {
            "valid": False,
            "reason": "Matrix dimensions do not match",
            "computed": computed.tolist(),
            "expected": expected,
        }

    for i in range(computed.rows):
        for j in range(computed.cols):

            difference = simplify(
                computed[i, j] - expected[i][j]
            )

            if difference != 0:
                return {
                    "valid": False,
                    "reason": "Matrix values do not match",
                    "row": i,
                    "column": j,
                    "computed": computed[i, j],
                    "expected": expected[i][j],
                }

    return {
        "valid": True
    }

def verify_numeric(question, solver):

    matrix = extract_matrix(question)

    expected = extract_answer(question)

    if expected is None:
        return False

    computed = solver(matrix)

    expected = float(expected)

    return abs(float(computed) - expected) < 1e-6

# -----------------------------------
# Topic Verifiers
# -----------------------------------

def verify_trace(question):

    return verify_numeric(question, trace)
    
def verify_determinant(question):

    return verify_numeric(question, determinant)

def verify_norm(question):

    return verify_numeric(question, norm)

def verify_rank(question):

    return verify_numeric(question, rank)

def verify_single_matrix_operation(question, solver):

    matrix = extract_matrix(question)

    expected = extract_answer_matrix(question)

    computed = solver(matrix)

    return compare_matrices(computed, expected)

def verify_matrix_operation(question, solver):

    matrices = extract_matrices(question)

    if len(matrices) < 2:
        return False

    A = matrices[0]
    B = matrices[1]

    expected = extract_answer_matrix(question)

    computed = solver(A, B)

    return compare_matrices(computed, expected)

def verify_multiplication(question):

    return verify_matrix_operation(question, multiply)

def verify_addition(question):

    return verify_matrix_operation(question, add)

def verify_subtraction(question):

    return verify_matrix_operation(question, subtract)

def verify_transpose(question):

    return verify_single_matrix_operation(question, transpose)

def verify_power(question):

    matrix = extract_matrix(question)

    power = extract_power(question)

    expected = extract_answer_matrix(question)

    computed = matrix_power(matrix, power)

    return compare_matrices(computed, expected)

def verify_inverse(question):

    return verify_single_matrix_operation(question, inverse)

def verify_rref(question):

    return verify_single_matrix_operation(question, rref)

def verify_nullspace(question):

    matrix = extract_matrix(question)

    expected = extract_answer_matrices(question)

    computed = nullspace(matrix)

    computed_vectors = [
        vector.tolist()
        for vector in computed
    ]

    return compare_matrix_lists(
        computed_vectors,
        expected
    )

def verify_column_space(question):

    matrix = extract_matrix(question)

    expected = extract_answer_matrices(question)

    computed = column_space(matrix)

    computed_vectors = [
        vector.tolist()
        for vector in computed
    ]

    return compare_matrix_lists(
        computed_vectors,
        expected
    )

def verify_eigenvalues(question):

    matrix = extract_matrix(question)

    expected = extract_eigenvalues(question)

    computed = eigenvalues(matrix)

    computed = expand_eigenvalues(computed)

    return computed == expected

def expand_eigenvalues(eigenvalue_dict):

    values = []

    for eigenvalue, multiplicity in eigenvalue_dict.items():

        for _ in range(multiplicity):
            values.append(eigenvalue)

    return values

def compare_eigenvectors(computed, expected):

    computed_matrix = Matrix(computed)
    expected_matrix = Matrix(expected)

    if computed_matrix.shape != expected_matrix.shape:
        return False

    if computed_matrix.is_zero_matrix:
        return expected_matrix.is_zero_matrix

    ratios = []

    for i in range(computed_matrix.rows):

        c = computed_matrix[i, 0]
        e = expected_matrix[i, 0]

        if e == 0:
            if c != 0:
                return False
        else:
            ratios.append(c / e)

    if not ratios:
        return False

    first_ratio = ratios[0]

    return all(
        simplify(ratio - first_ratio) == 0
        for ratio in ratios
    )

def verify_eigenvectors(question):

    matrix = extract_matrix(question)

    expected = extract_eigenvectors(question)

    computed_raw = eigenvectors(matrix)

    computed = {}

    for eigenvalue, multiplicity, vectors in computed_raw:

        computed[eigenvalue] = [
            vector.tolist()
            for vector in vectors
        ]

    if set(computed.keys()) != set(expected.keys()):
        return False

    for eigenvalue in computed:

        computed_vectors = computed[eigenvalue]
        expected_vector = expected[eigenvalue]

        if len(computed_vectors) != 1:
            return False

        if not compare_eigenvectors(
            computed_vectors[0],
            expected_vector
        ):
            return False

    return True

# -----------------------------------
# Dispatcher
# -----------------------------------

VERIFIERS = {
    TOPIC_TRACE: verify_trace,
    TOPIC_DETERMINANT: verify_determinant,
    TOPIC_RANK: verify_rank,
    TOPIC_NORM: verify_norm,
    TOPIC_MULTIPLICATION: verify_multiplication,
    TOPIC_ADDITION: verify_addition,
    TOPIC_SUBTRACTION: verify_subtraction,
    TOPIC_TRANSPOSE: verify_transpose,
    TOPIC_INVERSE: verify_inverse,
    TOPIC_POWER: verify_power,
    TOPIC_RREF: verify_rref,
    TOPIC_NULLSPACE: verify_nullspace,
    TOPIC_COLUMN_SPACE: verify_column_space,
    TOPIC_EIGENVALUES: verify_eigenvalues,
}
    
def verify(question):

    topic = extract_topic(question)

    verifier = VERIFIERS.get(topic)

    if verifier is None:
        return None

    return verifier(question)

