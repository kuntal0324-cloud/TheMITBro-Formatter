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
def validate(text):
    errors = []
    questions = split_questions(text)

    # -------------------------------------------------
    # Duplicate Question IDs
    # -------------------------------------------------

    question_ids = re.findall(
        r"##\s+([A-Z]{2}-[A-Z]{3}-\d{3})",
        text
    )

    seen = set()

    for qid in question_ids:

        if qid in seen:
            errors.append(f"Duplicate Question ID: {qid}")

        seen.add(qid)

    # -------------------------------------------------
    # Check balanced $$ blocks
    # -------------------------------------------------

    if text.count("$$") % 2 != 0:
        errors.append("Unmatched $$ display math block.")

    return errors
