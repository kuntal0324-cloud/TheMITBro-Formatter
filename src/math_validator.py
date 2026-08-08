from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------

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

Find the characteristic polynomial of A.

Latex

$$
\lambda^2 - 4\lambda + 6
$$

**Concept Tested:** Matrix Characteristic Polynomial
"""

print("Verify:", verify(question))
