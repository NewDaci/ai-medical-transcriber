import re

FILLER_WORDS = ["um", "uh", "you know", "like"]

def clean_text(text: str) -> str:
    text = text.lower()

    # remove filler words
    for word in FILLER_WORDS:
        text = text.replace(word, "")

    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text