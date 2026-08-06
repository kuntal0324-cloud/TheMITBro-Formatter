import re

def trace(matrix):
    return Matrix(matrix).trace()

def determinant(matrix):
    return Matrix(matrix).det()

def matrix_power(matrix, power):
    return Matrix(matrix) ** power

def multiply(A, B):
    return Matrix(A) * Matrix(B)

from sympy import Matrix
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

def verify_numeric(question, solver):

    matrix = extract_matrix(question)

    expected = extract_answer(question)

    if expected is None:
        return False

    computed = solver(matrix)

    return computed == int(expected)

def verify_trace(question):

    return verify_numeric(question, trace)
    
def verify_determinant(question):

    return verify_numeric(question, determinant)
    
def verify(question):

    topic = extract_topic(question)

    if topic == "Matrix Trace":
        return verify_trace(question)

    elif topic == "Determinant":
        return verify_determinant(question)

    return None
    
if __name__ == "__main__":

    question = """
### Question

Let

$$
A=
\\begin{bmatrix}
2 & -1\\\\
3 & 4
\\end{bmatrix}
$$

Find the determinant.

**Correct Answer:** 11

**Concept Tested:** Determinant
"""

    matrix = extract_matrix(question)

    print("Matrix:", matrix)
    print("Trace:", trace(matrix))
    print("Det:", determinant(matrix))
    print("Answer:", extract_answer(question))
    print("Verify:", verify(question))
    print("Topic:", extract_topic(question))
