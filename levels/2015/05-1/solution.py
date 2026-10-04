"""Solution for Advent of Code 2015, Day 5, Part 1."""

from collections.abc import Iterable


VOWELS = frozenset("aeiou")
FORBIDDEN_PAIRS = ("ab", "cd", "pq", "xy")


def is_nice(text: str) -> bool:
    """Return whether a string satisfies all three Part 1 niceness rules."""
    text = text.strip()
    has_three_vowels = sum(character in VOWELS for character in text) >= 3
    has_double_letter = any(
        left == right for left, right in zip(text, text[1:])
    )
    has_no_forbidden_pair = not any(pair in text for pair in FORBIDDEN_PAIRS)
    return has_three_vowels and has_double_letter and has_no_forbidden_pair


def count_nice_strings(strings: Iterable[str]) -> int:
    """Return how many input strings are nice."""
    return sum(is_nice(string) for string in strings)
