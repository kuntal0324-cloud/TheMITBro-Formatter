import re


def validate(text):
    errors = []

    # -------------------------------------------------
    # Unbalanced display math
    # -------------------------------------------------
    if text.count("$$") % 2 != 0:
        errors.append("Unmatched $$ block")

    # -------------------------------------------------
    # Unbalanced inline math
    # -------------------------------------------------
    if text.count(r"\(") != text.count(r"\)"):
        errors.append("Unmatched inline math")

    # -------------------------------------------------
    # Matrix environments
    # -------------------------------------------------
    if text.count(r"\begin{bmatrix}") != text.count(r"\end{bmatrix}"):
        errors.append("Unmatched bmatrix environment")

    # -------------------------------------------------
    # Broken LaTeX commands
    # -------------------------------------------------
    broken = [
        r"\$\(",
        r"\)\$",
        r"\$\$\\\(",
        r"\\\)\$\$",
    ]

    for pattern in broken:
        if re.search(pattern, text):
            errors.append(f"Broken LaTeX pattern: {pattern}")

    # -------------------------------------------------
    # Triple blank lines
    # -------------------------------------------------
    if re.search(r"\n{3,}", text):
        errors.append("More than two consecutive blank lines")

    # -------------------------------------------------
    # Duplicate separators
    # -------------------------------------------------
    if re.search(r"(?:\n---\s*){2,}", text):
        errors.append("Duplicate horizontal rules")

    return errors
