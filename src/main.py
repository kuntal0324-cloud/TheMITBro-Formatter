import os
import re
from pathlib import Path

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

OUTPUT_DIR.mkdir(exist_ok=True)

# -----------------------------
# Unicode replacements
# -----------------------------

UNICODE_MAP = {
    "²": "^2",
    "³": "^3",
    "⁴": "^4",
    "⁵": "^5",
    "⁶": "^6",
    "⁷": "^7",
    "⁸": "^8",
    "⁹": "^9",
    "⁰": "^0",
    "×": r"\times",
    "−": "-",
    "–": "-",
    "—": "-",
}


def replace_unicode(text):
    for old, new in UNICODE_MAP.items():
        text = text.replace(old, new)
    return text


# -----------------------------
# Replace unsupported commands
# -----------------------------

def fix_operatorname(text):

    text = text.replace(
        r"\operatorname{tr}",
        r"\mathrm{tr}"
    )

    text = text.replace(
        r"\operatorname{det}",
        r"\mathrm{det}"
    )

    text = text.replace(
        r"\operatorname{rank}",
        r"\mathrm{rank}"
    )

    text = text.replace(
        r"\operatorname{adj}",
        r"\mathrm{adj}"
    )

    return text


# -----------------------------
# Matrix detection
# -----------------------------

MATRIX_PATTERN = re.compile(
    r"""
    \[
    \s*
    (\d+|-?\d+)
    \s+
    (\d+|-?\d+)
    \s*
    \]
    \s*
    \[
    \s*
    (\d+|-?\d+)
    \s+
    (\d+|-?\d+)
    \s*
    \]
    """,
    re.VERBOSE,
)


def convert_matrix(match):

    a = match.group(1)
    b = match.group(2)
    c = match.group(3)
    d = match.group(4)

    return (
        "$$\n"
        "\\begin{bmatrix}\n"
        f"{a} & {b}\\\\\n"
        f"{c} & {d}\n"
        "\\end{bmatrix}\n"
        "$$"
    )
# -------------------------------------------------
# Equation formatter
# -------------------------------------------------

def fix_equations(text):

    replacements = {

        "tr(": r"\mathrm{tr}(",
        "det(": r"\mathrm{det}(",
        "rank(": r"\mathrm{rank}(",
        "adj(": r"\mathrm{adj}(",

        "Aᵀ": r"A^{T}",
        "Bᵀ": r"B^{T}",
        "A⁻¹": r"A^{-1}",
        "B⁻¹": r"B^{-1}",

        "|A|": r"\det(A)",
        "|B|": r"\det(B)",

        "A²": r"A^2",
        "A³": r"A^3",
        "A⁴": r"A^4",
        "A⁵": r"A^5",

        "B²": r"B^2",
        "B³": r"B^3",

        "Iₙ": r"I_n",

    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


# -------------------------------------------------
# Matrix conversion
# -------------------------------------------------

def convert_all_matrices(text):

    return MATRIX_PATTERN.sub(convert_matrix, text)


# -------------------------------------------------
# Complete formatter
# -------------------------------------------------

def format_document(text):

    text = replace_unicode(text)

    text = fix_operatorname(text)

    text = fix_equations(text)

    text = convert_all_matrices(text)

    return text


# -------------------------------------------------
# Process one markdown file
# -------------------------------------------------

def process_file(path):

    with open(path, "r", encoding="utf-8") as f:
        data = f.read()

    formatted = format_document(data)

    # Phase-1 Markdown cleanup
    formatted = re.sub(r"\n{3,}", "\n\n", formatted)
    formatted = re.sub(r"(?:\n---\s*){2,}", "\n---\n", formatted)
    formatted = re.sub(r"\\{2}mathrm", r"\\mathrm", formatted)
    formatted = formatted.rstrip() + "\n"

    out_file = OUTPUT_DIR / path.name

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(formatted)

    print(f"✓ {path.name}")
# -------------------------------------------------
# Main
# -------------------------------------------------

def main():

    files = list(INPUT_DIR.glob("*.md"))

    if not files:

        print("No markdown files found.")

        return

    for file in files:

        process_file(file)

    print("\nFormatting Complete.")


if __name__ == "__main__":

    main()
