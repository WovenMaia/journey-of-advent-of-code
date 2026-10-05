"""Solution for Advent of Code 2015, Day 12, Part 1."""

import json


def sum_numbers(value: object) -> int | float:
    """Return the sum of every JSON number nested in a decoded document."""
    if isinstance(value, bool):
        return 0
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, list):
        return sum(sum_numbers(item) for item in value)
    if isinstance(value, dict):
        return sum(sum_numbers(item) for item in value.values())
    return 0


def part_one(document: str) -> int | float:
    """Decode a JSON document and sum all numbers it contains."""
    return sum_numbers(json.loads(document))


if __name__ == "__main__":
    with open("inputs/2015/12.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
