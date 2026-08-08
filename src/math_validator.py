from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
if __name__ == "__main__":

    question = r"""
    $$
    A=
    \begin{bmatrix}
    1/2 & sqrt(2)\\
    pi & -3.5
    \end{bmatrix}
    $$
    """

    print("Matrix:", extract_matrix(question))
