from __future__ import annotations

def insert_newlines(text: str, every: int = 80) -> str:
    if every <= 0:
        return text
    return "\n".join(text[i : i + every] for i in range(0, len(text), every))

def normalize_string(value: str | None) -> str:
    return "" if value is None else str(value)
