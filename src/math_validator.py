from constants import *

from matrix_engine import *

# -----------------------------------
# Parsers
# -----------------------------------

from parsers import *
    
# -----------------------------------
# Verifier
# -----------------------------------

from verifiers import *

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
0 & 1
\end{bmatrix}
$$

Find A^3.

**Correct Answer:**

$$
\begin{bmatrix}
1 & 6\\
0 & 1
\end{bmatrix}
$$

**Concept Tested:** Matrix Power
"""

    matrices = extract_matrices(question)

    print("Matrices:", matrices)
    print(extract_answer_matrix(question))
    print("Verify:", verify(question))
    print(extract_power(question))
