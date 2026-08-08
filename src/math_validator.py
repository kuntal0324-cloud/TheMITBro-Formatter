from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------

print("Expected:", extract_characteristic_polynomial(question))
print("Computed:", characteristic_polynomial([[2, 0], [0, 3]]))
print("Verify:", verify_characteristic_polynomial(question))
