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
