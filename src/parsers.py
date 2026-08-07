import re

# -----------------------------------
# Parsers
# -----------------------------------

def extract_topic(question):

    match = re.search(
         r"\*\*Concept Tested:\*\*\s*(.+)",
         question
     )

    if not match:
         return None

    return match.group(1).strip()
    
def extract_answer(question):
    
    match = re.search(
        r"\*\*Correct Answer:\*\*\s*(.+)",
        question
    )

    if not match:
        return None

    return match.group(1).strip()

def parse_number(value):
    try:
        return int(value)

    except ValueError:

        try:
            return float(value)

        except ValueError:
            return value

def parse_matrix(matrix_text):
    
    rows = matrix_text.split("\\\\")

    cleaned = []

    for row in rows:

        row = row.strip()

        values = row.split("&")

        numbers = []

        for value in values:

            value = value.strip()

            numbers.append(parse_number(value))

        cleaned.append(numbers)

    return cleaned
    
def extract_matrix(question):

    match = re.search(
        r"\\begin{bmatrix}(.*?)\\end{bmatrix}",
        question,
        flags=re.DOTALL
    )

    if not match:
        return None

    matrix_text = match.group(1)
    
    return parse_matrix(matrix_text)
    
def extract_matrices(question):

    matches = re.findall(
        r"\\begin{bmatrix}(.*?)\\end{bmatrix}",
        question,
        flags=re.DOTALL
    )

    parsed = []

    for matrix_text in matches:
        parsed.append(parse_matrix(matrix_text))

    return parsed

def extract_answer_matrix(question):

    match = re.search(
        r"\*\*Correct Answer:\*\*.*?\\begin{bmatrix}(.*?)\\end{bmatrix}",
        question,
        flags=re.DOTALL
    )

    if not match:
        return None

    matrix_text = match.group(1)

    return parse_matrix(matrix_text)

def extract_power(question):

    match = re.search(
        r"A\^(\d+)",
        question
    )

    if not match:
        return None

    return int(match.group(1))
