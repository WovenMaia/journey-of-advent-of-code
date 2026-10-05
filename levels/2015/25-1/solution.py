"""Solution for Advent of Code 2015, Day 25, Part 1."""

import re

START = 20151125
MULTIPLIER = 252533
MODULUS = 33554393


def parse_target(document: str) -> tuple[int, int]:
    match = re.search(r"row (\d+), column (\d+)", document)
    if match is None:
        raise ValueError("expected row and column")
    row, column = map(int, match.groups())
    if row <= 0 or column <= 0:
        raise ValueError("row and column must be positive")
    return row, column


def code_at(row: int, column: int) -> int:
    diagonal = row + column - 1
    position = diagonal * (diagonal - 1) // 2 + column
    return START * pow(MULTIPLIER, position - 1, MODULUS) % MODULUS


def part_one(document: str) -> int:
    return code_at(*parse_target(document))


if __name__ == "__main__":
    with open("inputs/2015/25.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
