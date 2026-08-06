import re


def remove_trailing_spaces(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines())


def collapse_blank_lines(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text)


def remove_duplicate_rules(text: str) -> str:
    return re.sub(r"(?:\n---\s*){2,}", "\n---\n", text)


def normalize_headings(text: str) -> str:
    return re.sub(r"^(#+)\s*", lambda m: m.group(1) + " ", text, flags=re.MULTILINE)


def normalize_metadata(text: str) -> str:

    fields = [
        "Difficulty",
        "Type",
        "Marks",
        "Topic",
        "Correct Answer",
        "Concept Tested",
        "Tags",
    ]

    for field in fields:
        text = re.sub(
            rf"\*\*{field}:\*\*\s*",
            f"**{field}:** ",
            text,
        )

    return text


def remove_trailing_blank_lines(text: str) -> str:
    return text.rstrip() + "\n"


def format_markdown(text: str) -> str:

    text = remove_trailing_spaces(text)

    text = collapse_blank_lines(text)

    text = remove_duplicate_rules(text)

    text = normalize_headings(text)

    text = normalize_metadata(text)

    text = remove_trailing_blank_lines(text)

    return text
