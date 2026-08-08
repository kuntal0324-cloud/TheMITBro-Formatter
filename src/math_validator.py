from constants import *

from matrix_engine import *

from parsers import *

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
2 & 0\\
0 & 3
\end{bmatrix}
$$

Find the eigenvectors of A.

**Correct Answer:**

Eigenvalue 2:
\begin{bmatrix}
1\\
0
\end{bmatrix}

Eigenvalue 3:
\begin{bmatrix}
0\\
1
\end{bmatrix}

**Concept Tested:** Matrix Eigenvectors
"""

    matrix = extract_matrix(question)
    expected = extract_eigenvectors(question)
    raw = eigenvectors(matrix)

    print("Matrix:", matrix)
    print("Expected:", expected)
    print("Raw:", raw)

    computed = {}

    for eigenvalue, multiplicity, vectors in raw:
        computed[eigenvalue] = [
            vector.tolist()
            for vector in vectors
        ]

    print("Computed:", computed)

    print("Keys expected:", set(expected.keys()))
    print("Keys computed:", set(computed.keys()))

    print("Verify:", verify_eigenvectors(question))
