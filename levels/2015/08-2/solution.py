"""Solution for Advent of Code 2015, Day 8, Part 2."""

from collections.abc import Iterable


def encoded_length(literal: str) -> int:
    """Return the length of the re-encoded representation of one literal."""
    if len(literal) < 2 or literal[0] != '"' or literal[-1] != '"':
        raise ValueError(f"invalid string literal: {literal!r}")

    # The new surrounding quotes add two characters. Every quote and
    # backslash already present in the source must gain one escape character.
    return 2 + len(literal) + literal.count('"') + literal.count("\\")


def total_difference(lines: Iterable[str]) -> int:
    """Return total encoded length minus original code length."""
    difference = 0
    for raw_line in lines:
        literal = raw_line.rstrip("\r\n")
        difference += encoded_length(literal) - len(literal)
    return difference
