MEDICAL_DICT = {
    "diabities": "diabetes",
    "hypertansion": "hypertension",
    "asthama": "asthma",
    "feaver": "fever",
    "thb": "thumb",
    "traa": "trauma",
    "thick wear of the ends": "de quervain's",
    "synovitis": "tenosynovitis",
    "de quervain's tenosynovitis": "de quervain's tenosynovitis",
    "osteoarthritis": "osteoarthritis",
    "corticosteroids": "corticosteroid injection",
}

KNOWN_CONDITIONS = ["diabetes", "hypertension", "asthma", "fever", "de quervain's tenosynovitis", "osteoarthritis", "tenosynovitis"]

def correct_medical_terms(text: str):
    text = text.lower()

    # Apply corrections from MEDICAL_DICT
    for wrong, correct in MEDICAL_DICT.items():
        text = text.replace(wrong, correct)

    MEDICAL_TERMS = [
        "diabetes",
        "hypertension",
        "chest pain",
        "fever",
        "breathing",
        "light-headed",
        "de quervain's tenosynovitis",
        "osteoarthritis",
        "tenosynovitis",
        "hand pain",
        "wrist pain",
        "thumb pain"
    ]

    conditions = []

    for term in MEDICAL_TERMS:
        if term in text:
            # check negation
            if f"no {term}" in text or f"not {term}" in text or f"haven't {term}" in text:
                continue
            conditions.append(term)

    return text, conditions