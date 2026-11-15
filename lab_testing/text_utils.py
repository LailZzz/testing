UA_VOWELS = set("аеєиіїоуюяАЕЄИІЇОУЮЯ")
EN_VOWELS = set("aeiouyAEIOUY")
VOWELS = UA_VOWELS | EN_VOWELS


def count_symbols(text: str) -> int:
    return len(text)


def count_vowels(text: str) -> int:
    return sum(1 for ch in text if ch in VOWELS)


def divide(a, b):
    return a / b
