from __future__ import annotations

def universal_simplify_exception(exc: BaseException) -> str:
    return f"{type(exc).__name__}: {exc}"
