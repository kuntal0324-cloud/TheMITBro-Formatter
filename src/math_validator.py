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
    """

    matrix = extract_matrix(question)

print("Matrix:", matrix)
print("Trace:", trace(matrix))
print("Det:", determinant(matrix))
