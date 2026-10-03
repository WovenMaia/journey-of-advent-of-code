"""Solution for Advent of Code 2015, Day 3, Part 1."""

MOVES = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
}


def houses_visited(directions: str) -> int:
    """Return the number of distinct houses visited by Santa."""
    x = 0
    y = 0
    visited = {(x, y)}

    for position, direction in enumerate(directions.strip(), start=1):
        try:
            delta_x, delta_y = MOVES[direction]
        except KeyError as error:
            raise ValueError(
                f"unexpected direction {direction!r} at position {position}"
            ) from error
        x += delta_x
        y += delta_y
        visited.add((x, y))

    return len(visited)
