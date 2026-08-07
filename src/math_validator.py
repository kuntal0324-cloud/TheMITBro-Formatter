import re
from sympy import Matrix

# -----------------------------------
# Topic Constants
# -----------------------------------

TOPIC_TRACE = "Matrix Trace"
TOPIC_DETERMINANT = "Determinant"
TOPIC_RANK = "Matrix Rank"
TOPIC_NORM = "Matrix Norm"
TOPIC_MULTIPLICATION = "Matrix Multiplication"
TOPIC_ADDITION = "Matrix Addition"
TOPIC_SUBTRACTION = "Matrix Subtraction"
TOPIC_TRANSPOSE = "Matrix Transpose"
TOPIC_INVERSE = "Matrix Inverse"

# -----------------------------------
# Matrix Engine
# -----------------------------------

def trace(matrix):
    return Matrix(matrix).trace()
    

def determinant(matrix):
    return Matrix(matrix).det()

def rank(matrix):
    return Matrix(matrix).rank()

def norm(matrix):
    return Matrix(matrix).norm()

def matrix_power(matrix, power):
    return Matrix(matrix) ** power

def multiply(A, B):
    return Matrix(A) * Matrix(B)

def add(A, B):
    return Matrix(A) + Matrix(B)

def subtract(A, B):
    return Matrix(A) - Matrix(B)

def transpose(matrix):
    return Matrix(matrix).T

def inverse(matrix):
    return Matrix(matrix).inv()

# -----------------------------------
# Parsers
# -----------------------------------

def extract_topic(question):

    match = re.search(
         r"\*\*Concept Tested:\*\*\s*(.+)",
         question
     )

    if not match:
         return None

    return match.group(1).strip()
    
def extract_answer(question):
    
    match = re.search(
        r"\*\*Correct Answer:\*\*\s*(.+)",
        question
    )

    if not match:
        return None

    return match.group(1).strip()
    
def extract_matrix(question):

    match = re.search(
        r"\\begin{bmatrix}(.*?)\\end{bmatrix}",
        question,
        flags=re.DOTALL
    )

    if not match:
        return None

    matrix_text = match.group(1)
    
    rows = matrix_text.split("\\\\")

    cleaned = []
    
    for row in rows:

        row = row.strip()

        values = row.split("&")

        numbers = []

        for value in values:

            value = value.strip()

            numbers.append(int(value))

        cleaned.append(numbers)

    return cleaned
    
def extract_matrices(question):

    matches = re.findall(
        r"\\begin{bmatrix}(.*?)\\end{bmatrix}",
        question,
        flags=re.DOTALL
    )

    parsed = []

    for matrix_text in matches:

        rows = matrix_text.split("\\\\")

        cleaned = []

        for row in rows:

            row = row.strip()

            values = row.split("&")

            numbers = []

            for value in values:

                value = value.strip()

                numbers.append(int(value))

            cleaned.append(numbers)

        parsed.append(cleaned)

    return parsed

def extract_answer_matrix(question):

    match = re.search(
        r"\*\*Correct Answer:\*\*.*?\\begin{bmatrix}(.*?)\\end{bmatrix}",
        question,
        flags=re.DOTALL
    )

    if not match:
        return None

    matrix_text = match.group(1)

    rows = matrix_text.split("\\\\")

    cleaned = []

    for row in rows:

        row = row.strip()

        values = row.split("&")

        numbers = []

        for value in values:

            value = value.strip()

            numbers.append(int(value))

        cleaned.append(numbers)

    return cleaned
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
}
    
def verify(question):

    topic = extract_topic(question)

    verifier = VERIFIERS.get(topic)

    if verifier is None:
        return None

    return verifier(question)

# -----------------------------------
# Testing
# -----------------------------------
    
if __name__ == "__main__":

    question = r"""
### Question

Let

$$
A=
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix}
$$

Find the transpose of A.

**Correct Answer:**

$$
\begin{bmatrix}
1 & 4\\
2 & 5\\
3 & 6
\end{bmatrix}
$$

**Concept Tested:** Matrix Transpose
"""

    matrices = extract_matrices(question)

    print("Matrices:", matrices)
    print(extract_answer_matrix(question))
    print("Verify:", verify(question))
