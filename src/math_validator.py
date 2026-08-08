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
1 & 2\\
2 & 4
\end{bmatrix}
$$

Find a basis for the column space of A.

**Correct Answer:**

$$
\left\{
\begin{bmatrix}
1\\
2
\end{bmatrix}
\right\}
$$

**Concept Tested:** Matrix Column Space
"""

print("Verify:", verify(question))
