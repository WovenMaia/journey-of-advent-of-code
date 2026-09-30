"""Solution for Advent of Code 2015, Day 1, Part 2."""


def first_basement_position(instructions: str) -> int | None:
    """Return the one-based position that first reaches floor minus one."""
    floor = 0

    for position, instruction in enumerate(instructions.strip(), start=1):
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        else:
            raise ValueError(
                f"unexpected instruction {instruction!r} at position {position}"
            )

        if floor == -1:
            return position

    return None
