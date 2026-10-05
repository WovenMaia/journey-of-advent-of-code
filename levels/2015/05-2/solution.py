"""Solution for Advent of Code 2015, Day 5, Part 2."""

from collections.abc import Iterable


def has_repeated_pair(text: str) -> bool:
    """Return whether any two-letter pair recurs without overlapping."""
    first_seen: dict[str, int] = {}
    for index in range(len(text) - 1):
        pair = text[index : index + 2]
        previous_index = first_seen.get(pair)
        if previous_index is not None and index - previous_index > 1:
            return True
        if previous_index is None:
            first_seen[pair] = index
    return False


def has_repeat_with_gap(text: str) -> bool:
    """Return whether a letter repeats with exactly one letter between."""
    return any(left == right for left, right in zip(text, text[2:]))


def is_nice(text: str) -> bool:
    """Return whether a string satisfies both Part 2 niceness rules."""
    text = text.strip()
    return has_repeated_pair(text) and has_repeat_with_gap(text)


def count_nice_strings(strings: Iterable[str]) -> int:
    """Return how many input strings are nice."""
    return sum(is_nice(string) for string in strings)
