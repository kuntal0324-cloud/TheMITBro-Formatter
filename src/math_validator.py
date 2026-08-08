from constants import *

from matrix_engine import *

from parsers import *

from verifiers import *

# -----------------------------------
# Testing
# -----------------------------------
    
if __name__ == "__main__":

    try:
        print(parse_number("abc@@"))
    except Exception as e:
        print("Invalid input handled:", type(e).__name__)

print(parse_number("1.5"))
print(parse_number("1/2"))
print(parse_number("sqrt(2)"))
print(parse_number("pi"))

