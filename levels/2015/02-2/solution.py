"""Solution for Advent of Code 2015, Day 2, Part 2."""


def ribbon_for_present(dimensions: str) -> int:
    """Return ribbon required for one LxWxH present."""
    try:
        length, width, height = (int(value) for value in dimensions.split("x"))
    except ValueError as error:
        raise ValueError(f"invalid dimensions {dimensions!r}") from error

    if min(length, width, height) <= 0:
        raise ValueError(f"dimensions must be positive: {dimensions!r}")

    shortest_perimeter = 2 * sum(sorted((length, width, height))[:2])
    bow = length * width * height
    return shortest_perimeter + bow


def total_ribbon(presents: str) -> int:
    """Return ribbon required for newline-separated present dimensions."""
    return sum(
        ribbon_for_present(dimensions)
        for dimensions in presents.splitlines()
        if dimensions.strip()
    )
