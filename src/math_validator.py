from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------

question = r"""
### Question

Diagonalize the matrix

$$
A=
\begin{bmatrix}
4 & 1\\
2 & 3
\end{bmatrix}
$$

Find matrices P and D such that

$$
A=PDP^{-1}
$$

**Correct Answer:**

P =
$$
\begin{bmatrix}
-1 & 1\\
2 & 1
\end{bmatrix}
$$

D =
$$
\begin{bmatrix}
2 & 0\\
0 & 5
\end{bmatrix}
$$

**Concept Tested:** Matrix Diagonalization
"""

matrix = extract_matrix(question)

P, D = diagonalize_matrix(matrix)

print("P:")
print(P)

print("D:")
print(D)

print("Reconstructed:")
print(P * D * P.inv())

print("Verify:", P * D * P.inv() == Matrix(matrix))
