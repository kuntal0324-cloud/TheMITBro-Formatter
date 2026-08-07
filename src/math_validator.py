import re
from sympy import Matrix

# -----------------------------------
# Topic Constants
# -----------------------------------

TOPIC_TRACE = "Matrix Trace"
TOPIC_DETERMINANT = "Determinant"
TOPIC_RANK = "Matrix Rank"
TOPIC_NORM = "Matrix Norm"

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

VERIFIERS = {
    TOPIC_TRACE: verify_trace,
    TOPIC_DETERMINANT: verify_determinant,
    TOPIC_RANK: verify_rank,
    TOPIC_NORM: verify_norm,
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
1 & 2\\
3 & 4
\end{bmatrix}
$$

and

$$
B=
\begin{bmatrix}
5 & 6\\
7 & 8
\end{bmatrix}
$$

Find AB.
"""

    matrices = extract_matrices(question)

    print("Matrices:", matrices)
    print("Norm:", norm(matrices))
    print("Trace:", trace(matrices))
    print("Det:", determinant(matrices))
    print("Answer:", extract_answer(question))
    print("Rank:", rank(matrices))
    print("Topic:", extract_topic(question))
    print("Verify:", verify(question))
    print(extract_matrices(question))
