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
1 & 2\\
2 & 4
\end{bmatrix}
$$

Find the nullspace of A.

**Correct Answer:**

$$
\left\{
\begin{bmatrix}
-2\\
1
\end{bmatrix}
\right\}
$$

**Concept Tested:** Matrix Nullspace
"""

    print("Matrices:", extract_matrices(question))
    print("Verify:", verify(question))
