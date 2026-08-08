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
4 & 2\\
1 & 3
\end{bmatrix}
$$

Find the eigenvectors of A.

**Correct Answer:**

Eigenvalue 5:
\begin{bmatrix}
2\\
1
\end{bmatrix}

Eigenvalue 2:
\begin{bmatrix}
-1\\
1
\end{bmatrix}

**Concept Tested:** Matrix Eigenvectors
"""

print("Verify:", verify(question))
