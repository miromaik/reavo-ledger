from flags import WEIGHTS

def calculate_rating(flags: list[str]) -> str:
    score = sum(WEIGHTS[f] for f in flags)

    if score == 0:
        return "A"
    if score <= 2:
        return "B"
    if score <= 4:
        return "C"
    if score <= 6:
        return "D"
    if score <= 8:
        return "E"
    return "F"
