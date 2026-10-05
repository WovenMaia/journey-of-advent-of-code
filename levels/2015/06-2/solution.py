"""Solution for Advent of Code 2015, Day 6, Part 2."""

from array import array
from collections.abc import Iterable
import re


GRID_SIZE = 1_000
_INSTRUCTION = re.compile(
    r"^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$"
)


def total_brightness(instructions: Iterable[str]) -> int:
    """Apply the instructions and return the combined brightness."""
    grid = [array("I", [0]) * GRID_SIZE for _ in range(GRID_SIZE)]

    for raw_instruction in instructions:
        instruction = raw_instruction.strip()
        match = _INSTRUCTION.fullmatch(instruction)
        if match is None:
            raise ValueError(f"invalid instruction: {raw_instruction!r}")

        operation, left, top, right, bottom = match.groups()
        x1, y1, x2, y2 = map(int, (left, top, right, bottom))
        if not (0 <= x1 <= x2 < GRID_SIZE and 0 <= y1 <= y2 < GRID_SIZE):
            raise ValueError(f"coordinates out of range: {raw_instruction!r}")

        for row_index in range(y1, y2 + 1):
            row = grid[row_index]
            if operation == "turn on":
                for column in range(x1, x2 + 1):
                    row[column] += 1
            elif operation == "turn off":
                for column in range(x1, x2 + 1):
                    if row[column] > 0:
                        row[column] -= 1
            else:
                for column in range(x1, x2 + 1):
                    row[column] += 2

    return sum(map(sum, grid))
