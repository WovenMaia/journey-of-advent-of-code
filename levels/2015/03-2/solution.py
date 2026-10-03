"""Solution for Advent of Code 2015, Day 3, Part 2."""

MOVES = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
}


def houses_visited_with_robot(directions: str) -> int:
    """Return distinct houses visited by alternating Santa and Robo-Santa."""
    positions = [(0, 0), (0, 0)]
    visited = {(0, 0)}

    for position, direction in enumerate(directions.strip(), start=1):
        try:
            delta_x, delta_y = MOVES[direction]
        except KeyError as error:
            raise ValueError(
                f"unexpected direction {direction!r} at position {position}"
            ) from error

        mover = (position - 1) % 2
        x, y = positions[mover]
        destination = (x + delta_x, y + delta_y)
        positions[mover] = destination
        visited.add(destination)

    return len(visited)
