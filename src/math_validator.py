from sympy import Matrix

def trace(matrix):

    return Matrix(matrix).trace()

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

    cleaned.append(values)

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

    print(extract_matrix(question))
