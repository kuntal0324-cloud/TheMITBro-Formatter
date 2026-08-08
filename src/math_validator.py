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

Find the characteristic polynomial of

$$
A=
\begin{bmatrix}
2 & 0\\
0 & 3
\end{bmatrix}
$$

**Correct Answer:**

$$
\lambda^2-5\lambda+6
$$

**Concept Tested:** Characteristic Polynomial
"""

matrix = [[2, 0], [0, 3]]

print("Characteristic Polynomial:",
      characteristic_polynomial(matrix))
