from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
if __name__ == "__main__":

    question = r"""
**Correct Answer:** 2, 3, 5, 5
"""

    print("Eigenvalues:", extract_eigenvalues(question))
