import re


def is_url_valid(url: str) -> bool:
    return bool(re.match(r"^https?://", url))
