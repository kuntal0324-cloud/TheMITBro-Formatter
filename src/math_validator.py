from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
if __name__ == "__main__":

    from parsers import parse_number

print(parse_number("1.5"))
print(parse_number("1/2"))
print(parse_number("sqrt(2)"))
print(parse_number("pi"))
print(parse_number("-2"))
