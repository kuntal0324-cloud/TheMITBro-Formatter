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

    return match.group(1)

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
