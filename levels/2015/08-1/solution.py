"""Solution for Advent of Code 2015, Day 8, Part 1."""

from collections.abc import Iterable
import string


_HEX_DIGITS = frozenset(string.hexdigits)


def memory_length(literal: str) -> int:
    """Return the number of characters represented by one string literal."""
    if len(literal) < 2 or literal[0] != '"' or literal[-1] != '"':
        raise ValueError(f"invalid string literal: {literal!r}")

    length = 0
    index = 1
    end = len(literal) - 1
    while index < end:
        if literal[index] != "\\":
            length += 1
            index += 1
            continue

        if index + 1 >= end:
            raise ValueError(f"invalid escape in string literal: {literal!r}")
        if literal[index + 1] == "x":
            if (
                index + 3 >= end
                or literal[index + 2] not in _HEX_DIGITS
                or literal[index + 3] not in _HEX_DIGITS
            ):
                raise ValueError(f"invalid hexadecimal escape: {literal!r}")
            index += 4
        elif literal[index + 1] in '\\"':
            index += 2
        else:
            raise ValueError(f"invalid escape in string literal: {literal!r}")
        length += 1

    return length


def total_difference(lines: Iterable[str]) -> int:
    """Return total code characters minus in-memory characters."""
    difference = 0
    for raw_line in lines:
        literal = raw_line.rstrip("\r\n")
        difference += len(literal) - memory_length(literal)
    return difference
