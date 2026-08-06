from sympy import Matrix

def trace(matrix):
    return Matrix(matrix).trace()

def determinant(matrix):
    return Matrix(matrix).det()

def matrix_power(matrix, power):
    return Matrix(matrix) ** power

def multiply(A, B):
    return Matrix(A) * Matrix(B)

import re

def extract_answer(question):
    def extract_topic(question):

        match = re.search(
            r"\*\*Concept Tested:\*\*\s*(.+)",
            question
        )

        if not match:
            return None

        return match.group(1).strip()

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
def verify_trace(question):

    matrix = extract_matrix(question)

    expected = extract_answer(question)

    if expected is None:
        return False

    computed = trace(matrix)

    return computed == int(expected)
def verify(question):

    return verify_trace(question)

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

    Find the trace.

    **Correct Answer:** 6

    **Concept Tested:** Matrix Trace
    """

    matrix = extract_matrix(question)

    print("Matrix:", matrix)
    print("Trace:", trace(matrix))
    print("Det:", determinant(matrix))
    print("Answer:", extract_answer(question))
    print("Verify:", verify(question))
    print("Topic:", extract_topic(question))
