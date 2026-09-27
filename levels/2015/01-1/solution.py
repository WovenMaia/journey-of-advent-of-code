"""Solution for Advent of Code 2015, Day 1, Part 1."""

from collections.abc import Iterator


def floor_trace(instructions: str) -> Iterator[int]:
    """Yield the running floor, including the starting floor of zero."""
    floor = 0
    yield floor

    for position, instruction in enumerate(instructions.strip(), start=1):
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        else:
            raise ValueError(
                f"unexpected instruction {instruction!r} at position {position}"
            )
        yield floor


def final_floor(instructions: str) -> int:
    """Return the floor reached after consuming every instruction."""
    floor = 0
    for floor in floor_trace(instructions):
        pass
    return floor
