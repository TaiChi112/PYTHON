def count_words(text: str) -> int:
    """Return the number of words split by whitespace."""
    return len(text.split())


def count_vowels(text: str) -> int:
    """Return the count of English vowels (a, e, i, o, u)."""
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)


def clean_text(text: str) -> str:
    """Trim surrounding spaces and convert text to lowercase."""
    return text.strip().lower()


def highlight(text: str) -> str:
    """Wrap the text with *** on both sides."""
    return f"*** {text} ***"
