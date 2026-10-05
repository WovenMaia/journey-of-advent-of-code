"""Solution for Advent of Code 2015, Day 17, Part 1."""

from functools import lru_cache


def parse_containers(document: str) -> tuple[int, ...]:
    """Parse one positive container capacity per non-empty input line."""
    capacities: list[int] = []
    for line in document.splitlines():
        if not line:
            continue
        try:
            capacity = int(line)
        except ValueError as error:
            raise ValueError(f"invalid container capacity: {line!r}") from error
        if capacity <= 0:
            raise ValueError(f"container capacity must be positive: {capacity}")
        capacities.append(capacity)
    return tuple(capacities)


def part_one(document: str, target: int = 150) -> int:
    """Count subsets of containers whose capacities sum to *target*."""
    containers = parse_containers(document)

    @lru_cache(maxsize=None)
    def count(index: int, remaining: int) -> int:
        if remaining == 0:
            return 1
        if index == len(containers) or remaining < 0:
            return 0
        return count(index + 1, remaining) + count(
            index + 1, remaining - containers[index]
        )

    return count(0, target)


if __name__ == "__main__":
    with open("inputs/2015/17.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
