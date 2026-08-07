import re
from sympy import Matrix

# -----------------------------------
# Topic Constants
# -----------------------------------

TOPIC_TRACE = "Matrix Trace"
TOPIC_DETERMINANT = "Determinant"
TOPIC_RANK = "Matrix Rank"

# -----------------------------------
# Matrix Engine
# -----------------------------------

def trace(matrix):
    return Matrix(matrix).trace()
    

def determinant(matrix):
    return Matrix(matrix).det()

def rank(matrix):
    return Matrix(matrix).rank()

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

# -----------------------------------
# Generic Verifier
# -----------------------------------

def verify_numeric(question, solver):

    matrix = extract_matrix(question)

    expected = extract_answer(question)

    if expected is None:
        return False

    computed = solver(matrix)

    return computed == int(expected)

# -----------------------------------
# Topic Verifiers
# -----------------------------------

def verify_trace(question):

    return verify_numeric(question, trace)
    
def verify_determinant(question):

    return verify_numeric(question, determinant)

def verify_rank(question):

    return verify_numeric(question, rank)

VERIFIERS = {
    TOPIC_TRACE: verify_trace,
    TOPIC_DETERMINANT: verify_determinant,
    TOPIC_RANK: verify_rank,
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

    question = """
### Question

Let

$$
A=
\begin{bmatrix}
1 & 2\\
2 & 4
\end{bmatrix}
$$

Find the rank.

**Correct Answer:** 1

**Concept Tested:** Matrix Rank

    matrix = extract_matrix(question)

    print("Matrix:", matrix)
    print("Trace:", trace(matrix))
    print("Det:", determinant(matrix))
    print("Answer:", extract_answer(question))
    print("Verify:", verify(question))
    print("Topic:", extract_topic(question))
    print("Verify:", verify(question))
