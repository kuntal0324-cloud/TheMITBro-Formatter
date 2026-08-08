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
0 & 2
\end{bmatrix}
$$

Find the eigenvectors of A.

**Correct Answer:**

Eigenvalue 2:

\begin{bmatrix}
1\\
0
\end{bmatrix}

\begin{bmatrix}
0\\
1
\end{bmatrix}

**Concept Tested:** Matrix Eigenvectors
"""

print("Verify:", verify(question))
