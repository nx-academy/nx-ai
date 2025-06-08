import re


def clean_md_for_rag(content):
    # Removing YAML's Front Matter
    content = re.sub(r"^---.*?---\s*", "", content, flags=re.DOTALL)

    # Removing HTML tags (article, br, img, etc.)
    content = re.sub(r"<(br|/?article|img[^>]*)>", "", content)

    # Removing Markdown images
    content = re.sub(r"!\[.*?\]\(.*?\)", "", content)

    # Removing multiple empty lines
    content = re.sub(r"\n{2,}", "\n\n", content)

    # Removing trailing spaces
    content = re.sub(r"[ \t]+$", "", content, flags=re.MULTILINE)

    return content.strip()
