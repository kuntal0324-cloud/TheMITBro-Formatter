from sympy import sympify
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

def is_valid_number_expression(value):

    pattern = r"^[0-9+\-*/().,\s_a-zA-Z]+$"

    return re.fullmatch(pattern, value) is not None

def parse_number(value):

    value = value.strip()

    if not is_valid_number_expression(value):
        raise ValueError("Invalid mathematical expression")

    return sympify(value)

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

def extract_answer_matrices(question):

    match = re.search(
        r"\*\*Correct Answer:\*\*(.*?)(?:\*\*Concept Tested:\*\*|$)",
        question,
        flags=re.DOTALL
    )

    if not match:
        return []

    answer_section = match.group(1)

    matches = re.findall(
        r"\\begin{bmatrix}(.*?)\\end{bmatrix}",
        answer_section,
        flags=re.DOTALL
    )

    return [
        parse_matrix(matrix_text)
        for matrix_text in matches
    ]

def extract_eigenvalues(question):

    answer = extract_answer(question)

    if answer is None:
        return None

    values = [
        parse_number(value.strip())
        for value in answer.split(",")
        if value.strip()
    ]

    return values

def extract_eigenvectors(question):

    matches = re.findall(
        r"Eigenvalue\s+([^\s:]+)\s*:\s*"
        r"\\begin{bmatrix}(.*?)\\end{bmatrix}",
        question,
        flags=re.DOTALL
    )

    parsed = {}

    for eigenvalue_text, vector_text in matches:

        eigenvalue = parse_number(eigenvalue_text)

        vector = parse_matrix(vector_text)

        parsed[eigenvalue] = vector

    return parsed
