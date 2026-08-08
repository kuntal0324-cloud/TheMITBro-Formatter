from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------

question = r"""
### Question

Find the inverse of the matrix

$$
A=
\begin{bmatrix}
4 & 7\\
2 & 6
\end{bmatrix}
$$

**Correct Answer:**
$$
A^{-1}=
\begin{bmatrix}
\frac{3}{5} & -\frac{7}{10}\\
-\frac{1}{5} & \frac{2}{5}
\end{bmatrix}
$$

**Concept Tested:** Matrix Inverse
"""

print("Verify:", verify(question))
