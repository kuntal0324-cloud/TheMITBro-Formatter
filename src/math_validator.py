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
