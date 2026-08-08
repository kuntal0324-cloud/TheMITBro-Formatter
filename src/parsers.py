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

    rows = re.split(r"\\{1,2}|\n", matrix_text)

    cleaned = []

    for row in rows:

        row = row.strip()

        if not row:
            continue

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

    blocks = re.findall(
        r"Eigenvalue\s+([^\s:]+)\s*:\s*(.*?)(?=Eigenvalue\s+|\*\*Concept Tested:\*\*|$)",
        question,
        flags=re.DOTALL
    )

    parsed = {}

    for eigenvalue_text, block_text in blocks:

        eigenvalue = parse_number(eigenvalue_text)

        vectors = re.findall(
            r"\\begin{bmatrix}(.*?)\\end{bmatrix}",
            block_text,
            flags=re.DOTALL
        )

        parsed[eigenvalue] = []

        for vector_text in vectors:

            vector = parse_matrix(vector_text)

            parsed[eigenvalue].append(vector)

    return parsed

def extract_characteristic_polynomial(question):

    match = re.search(
        r"\*\*Correct Answer:\*\*\s*\$\$(.*?)\$\$",
        question,
        flags=re.DOTALL
    )

    if not match:
        return None

    expression = match.group(1).strip()

    expression = expression.replace(r"\lambda", "x")
    expression = expression.replace("lambda", "x")

    from sympy.parsing.sympy_parser import (
        parse_expr,
        standard_transformations,
        implicit_multiplication,
        convert_xor
    )

    transformations = (
        standard_transformations
        + (implicit_multiplication, convert_xor)
    )

    return parse_expr(
        expression,
        transformations=transformations
    )

