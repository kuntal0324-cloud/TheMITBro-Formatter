from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------

if __name__ == "__main__":
    question = r"""
    ...
    """  
print("Expected:", extract_characteristic_polynomial(question))
print("Computed:", characteristic_polynomial([[2, 0], [0, 3]]))
print("Verify:", verify_characteristic_polynomial(question))

    
