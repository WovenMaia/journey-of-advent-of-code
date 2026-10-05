"""Solution for Advent of Code 2015, Day 9, Part 2."""

from collections.abc import Iterable
from itertools import permutations


def parse_distances(lines: Iterable[str]) -> dict[tuple[str, str], int]:
    """Parse pairwise distances, storing each undirected edge once."""
    distances: dict[tuple[str, str], int] = {}
    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        parts = line.split(" = ")
        if len(parts) != 2 or " to " not in parts[0]:
            raise ValueError(f"invalid distance: {raw_line!r}")
        left, right = parts[0].split(" to ", 1)
        if not left or not right:
            raise ValueError(f"invalid distance: {raw_line!r}")
        try:
            distance = int(parts[1])
        except ValueError as exc:
            raise ValueError(f"invalid distance: {raw_line!r}") from exc
        distances[tuple(sorted((left, right)))] = distance
    return distances


def longest_route(lines: Iterable[str]) -> int:
    """Return the longest route visiting every location exactly once."""
    distances = parse_distances(lines)
    locations = sorted({location for edge in distances for location in edge})
    if len(locations) < 2:
        raise ValueError("at least two locations are required")

    best: int | None = None
    for route in permutations(locations):
        distance = sum(
            distances[tuple(sorted((origin, destination)))]
            for origin, destination in zip(route, route[1:])
        )
        if best is None or distance > best:
            best = distance
    assert best is not None
    return best


if __name__ == "__main__":
    with open("inputs/2015/09.txt", encoding="utf-8") as input_file:
        print(longest_route(input_file))
