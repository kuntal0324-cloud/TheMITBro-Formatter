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

    return computed.tolist() == expected

def verify_matrix_operation(question, solver):

    matrices = extract_matrices(question)

    if len(matrices) < 2:
        return False

    A = matrices[0]
    B = matrices[1]

    expected = extract_answer_matrix(question)

    computed = solver(A, B)

    return computed.tolist() == expected

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

    return computed.tolist() == expected

def verify_inverse(question):

    return verify_single_matrix_operation(question, inverse)

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
}
    
def verify(question):

    topic = extract_topic(question)

    verifier = VERIFIERS.get(topic)

    if verifier is None:
        return None

    return verifier(question)

