import re
def split_questions(text):
    """
    Split a markdown document into individual questions.
    """
    pattern = r"(?=^##\s+[A-Z]{2}-[A-Z]{3}-\d{3})"

    questions = re.split(
        pattern,
        text,
        flags=re.MULTILINE
    )

    return [q.strip() for q in questions if q.strip()]

def validate_duplicate_ids(text):

    errors = []

    question_ids = re.findall(
        r"##\s+([A-Z]{2}-[A-Z]{3}-\d{3})",
        text
    )

    seen = set()

    for qid in question_ids:

        if qid in seen:
            errors.append(
                f"Duplicate Question ID: {qid}"
            )

        seen.add(qid)

    return errors

def validate_question_sequence(text):

    errors = []

    question_ids = re.findall(
        r"##\s+([A-Z]{2}-[A-Z]{3}-\d{3})",
        text
    )

    numbers = []

    for qid in question_ids:
        numbers.append(int(qid.split("-")[-1]))

    for i in range(len(numbers) - 1):

        expected = numbers[i] + 1

        if numbers[i + 1] != expected:
            errors.append(
                f"Question IDs out of sequence: {numbers[i]:03d} -> {numbers[i+1]:03d}"
            )

    return errors

def validate(text):
    errors = []
    
    questions = split_questions(text)

    errors.extend(validate_duplicate_ids(text))
    errors.extend(validate_question_sequence(text))
    
    for question in questions:
        qid = re.search(r"##\s+([A-Z]{2}-[A-Z]{3}-\d{3})",
        question)

        if not qid:
           continue

        required_sections = [
        "### Question",
        "**Correct Answer:**",
        "### Solution",
        "**Concept Tested:**",
        "**Tags:**"
        ]

        for section in required_sections:
            if section not in question:
               errors.append(f"{qid.group(1)}: Missing {section}")
    # -------------------------------------------------
    # MCQ Option Validation
    # -------------------------------------------------

        if "**Type:** MCQ" in question:

            options = re.findall(
            r"^\s*([A-D])\.",
            question,
            flags=re.MULTILINE
        )

        if options != ["A", "B", "C", "D"]:
            errors.append(
               f"{qid.group(1)}: Invalid MCQ options ({options})"
        ) 
            
    # -------------------------------------------------
    # Correct Answer Validation
    # -------------------------------------------------

    answer = re.search(
        r"\*\*Correct Answer:\*\*\s*(.+)",
        question
    )

    if answer:

        value = answer.group(1).strip()

        if "**Type:** MCQ" in question:

            if value not in ["A", "B", "C", "D"]:
                errors.append(
                    f"{qid.group(1)}: Invalid MCQ answer ({value})"
                )

        elif "**Type:** NAT" in question:

              if not re.fullmatch(r"-?\d+(\.\d+)?", value):
                  errors.append(
                      f"{qid.group(1)}: Invalid NAT answer ({value})"
                )
    # -------------------------------------------------
    # Check balanced $$ blocks
    # -------------------------------------------------

    question_ids = re.findall(
    r"##\s+([A-Z]{2}-[A-Z]{3}-\d{3})",
    text
    )

    if text.count("$$") % 2 != 0:
        errors.append("Unmatched $$ display math block.")

    def validate_question_sequence(text):

        errors = []

        question_ids = re.findall(
            r"##\s+([A-Z]{2}-[A-Z]{3}-\d{3})",
            text
        )

        numbers = []

        for qid in question_ids:
            numbers.append(int(qid.split("-")[-1]))

        for i in range(len(numbers) - 1):

            expected = numbers[i] + 1

            if numbers[i + 1] != expected:
                errors.append(
                    f"Question IDs out of sequence: {numbers[i]:03d} -> {numbers[i+1]:03d}"
                )

    return errors
