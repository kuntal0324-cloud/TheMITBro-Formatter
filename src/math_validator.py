from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
if __name__ == "__main__":

    print(parse_number("5"))
    print(parse_number("3.14"))
    print(parse_number("1/2"))
    print(parse_number("sqrt(2)"))
    print(parse_number("pi"))
