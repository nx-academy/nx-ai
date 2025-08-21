import re
import unicodedata


SLUG_RE = re.compile(r"[^a-z0-9\-]")


def _remove_accents(text: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )


def slugify_title(title: str) -> str:
    s = title.strip().lower().replace("’", "-")
    s = _remove_accents(s)
    s = re.sub(r"\s+", "-", s)
    s = SLUG_RE.sub("", s)
    s = re.sub(r"-{2,}", "-", s)
    return s[:80].strip("-")
