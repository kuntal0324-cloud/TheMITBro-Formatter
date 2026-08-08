from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
matrix = Matrix([
    [1, 2],
    [2, 4]
])

print("Column Space:")
print(column_space(matrix))
