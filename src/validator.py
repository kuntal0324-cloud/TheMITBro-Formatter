import re

def validate(text):
    errors = []

    # Check balanced $$ blocks
    if text.count("$$") % 2 != 0:
        errors.append("Unmatched $$ display math block.")

    return errors
