import re

SLUG_RE = re.compile(r"[^a-z0-9-]+")


def slugify_title(title: str) -> str:
    s = title.strip().lower().replace("’", "'")
    s = re.sub(r"\s+", "-", s)
    s = SLUG_RE.sub("", s)
    return s[:80].strip("-")
