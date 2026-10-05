"""Solution for Advent of Code 2015, Day 12, Part 2."""

import json


def sum_non_red(value: object) -> int | float:
    """Return the sum after excluding objects containing a red-valued property."""
    if isinstance(value, bool):
        return 0
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, list):
        return sum(sum_non_red(item) for item in value)
    if isinstance(value, dict):
        if "red" in value.values():
            return 0
        return sum(sum_non_red(item) for item in value.values())
    return 0


def part_two(document: str) -> int | float:
    """Decode a JSON document and sum numbers outside red-containing objects."""
    return sum_non_red(json.loads(document))


if __name__ == "__main__":
    with open("inputs/2015/12.txt", encoding="utf-8") as input_file:
        print(part_two(input_file.read()))
