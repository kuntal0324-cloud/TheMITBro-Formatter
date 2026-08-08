from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------

if __name__ == "__main__":

    question = r"""
**Correct Answer:**

Eigenvalue 2:
\begin{bmatrix}
1\\
2
\end{bmatrix}

Eigenvalue 3:
\begin{bmatrix}
1\\
-1
\end{bmatrix}
"""

print("Eigenvectors:", extract_eigenvectors(question))
