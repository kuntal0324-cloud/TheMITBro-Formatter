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

Find the eigenvalues of A.

**Correct Answer:** 2, 3

**Concept Tested:** Eigenvalues
"""

    print("Verify:", verify_eigenvalues(question))
