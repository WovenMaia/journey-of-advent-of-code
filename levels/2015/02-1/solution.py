"""Solution for Advent of Code 2015, Day 2, Part 1."""


def paper_for_present(dimensions: str) -> int:
    """Return wrapping paper required for one LxWxH present."""
    try:
        length, width, height = (int(value) for value in dimensions.split("x"))
    except ValueError as error:
        raise ValueError(f"invalid dimensions {dimensions!r}") from error

    if min(length, width, height) <= 0:
        raise ValueError(f"dimensions must be positive: {dimensions!r}")

    side_areas = (length * width, width * height, height * length)
    return 2 * sum(side_areas) + min(side_areas)


def total_paper(presents: str) -> int:
    """Return paper required for newline-separated present dimensions."""
    return sum(
        paper_for_present(dimensions)
        for dimensions in presents.splitlines()
        if dimensions.strip()
    )
