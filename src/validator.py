import re

def validate(text):
    errors = []
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

    # Check balanced $$ blocks
    if text.count("$$") % 2 != 0:
        errors.append("Unmatched $$ display math block.")

    return errors
