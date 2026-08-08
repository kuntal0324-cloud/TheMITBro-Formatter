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

**Correct Answer**

$$
\lambda^2 - 5\lambda + 6
$$

**Concept Tested:** Matrix Characteristic Polynomial
"""

print("Topic:", extract_topic(question))
print("Expected:", extract_characteristic_polynomial(question))
print("Computed:", characteristic_polynomial(extract_matrix(question)))
print("Direct:", verify_characteristic_polynomial(question))
print("Dispatcher:", verify(question))
