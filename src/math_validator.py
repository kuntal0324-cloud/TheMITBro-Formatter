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

Find the RREF of A.

**Correct Answer:**

$$
\begin{bmatrix}
1 & 2\\
0 & 0
\end{bmatrix}
$$

**Concept Tested:** Matrix RREF
"""

    print("Verify:", verify(question))
