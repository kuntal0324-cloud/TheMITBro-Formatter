import re


def normalize_display_math(text: str) -> str:
    # \[ ... \] -> $$ ... $$
    text = re.sub(
        r"\\\[\s*(.*?)\s*\\\]",
        lambda m: "\n$$\n" + m.group(1).strip() + "\n$$\n",
        text,
        flags=re.DOTALL,
    )
    return text


def normalize_inline_math(text: str) -> str:
    # $...$ -> \(...\)
    text = re.sub(
        r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)",
        lambda m: r"\(" + m.group(1) + r"\)",
        text,
    )
    return text


def normalize_det(text: str) -> str:
    text = text.replace(r"\det(", r"\mathrm{det}(")
    return text


def normalize_trace(text: str):
    text = text.replace(r"\operatorname{tr}", r"\mathrm{tr}")
    return text


def latex_cleanup(text: str):

    text = normalize_display_math(text)

    text = normalize_det(text)

    text = normalize_trace(text)

    return text
