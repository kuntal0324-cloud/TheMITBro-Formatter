from sympy import Matrix

def trace(matrix):

    return Matrix(matrix).trace()

def extract_matrix(question):
    pass

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
