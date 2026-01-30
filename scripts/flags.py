FLAGS = {
    "AI_TRAINING": ["train", "training", "machine learning", "ai"],
    "PERPETUAL_LICENSE": ["perpetual", "irrevocable"],
    "DATA_SHARING": ["third party", "share", "affiliate"],
    "TRACKING": ["tracking", "cookies", "analytics"],
    "ACCOUNT_TERMINATION": ["terminate", "suspend"],
}

WEIGHTS = {
    "AI_TRAINING": 3,
    "PERPETUAL_LICENSE": 3,
    "DATA_SHARING": 2,
    "TRACKING": 2,
    "ACCOUNT_TERMINATION": 1,
}

def detect_flags(text: str):
    text = text.lower()
    found = []

    for flag, keywords in FLAGS.items():
        if any(k in text for k in keywords):
            found.append(flag)

    return found
