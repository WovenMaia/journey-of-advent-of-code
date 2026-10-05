"""Solution for Advent of Code 2015, Day 6, Part 1."""

from collections.abc import Iterable
import re


GRID_SIZE = 1_000
_INSTRUCTION = re.compile(
    r"^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$"
)
_TOGGLE_TABLE = bytes.maketrans(b"\x00\x01", b"\x01\x00")


def count_lit(instructions: Iterable[str]) -> int:
    """Apply the instructions and return the number of lit lights."""
    grid = [bytearray(GRID_SIZE) for _ in range(GRID_SIZE)]

    for raw_instruction in instructions:
        instruction = raw_instruction.strip()
        match = _INSTRUCTION.fullmatch(instruction)
        if match is None:
            raise ValueError(f"invalid instruction: {raw_instruction!r}")

        operation, left, top, right, bottom = match.groups()
        x1, y1, x2, y2 = map(int, (left, top, right, bottom))
        if not (0 <= x1 <= x2 < GRID_SIZE and 0 <= y1 <= y2 < GRID_SIZE):
            raise ValueError(f"coordinates out of range: {raw_instruction!r}")

        width = x2 - x1 + 1
        if operation == "turn on":
            replacement = b"\x01" * width
            for row_index in range(y1, y2 + 1):
                grid[row_index][x1 : x2 + 1] = replacement
        elif operation == "turn off":
            replacement = b"\x00" * width
            for row_index in range(y1, y2 + 1):
                grid[row_index][x1 : x2 + 1] = replacement
        else:
            for row_index in range(y1, y2 + 1):
                row = grid[row_index]
                row[x1 : x2 + 1] = row[x1 : x2 + 1].translate(_TOGGLE_TABLE)

    return sum(map(sum, grid))
