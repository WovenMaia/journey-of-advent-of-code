"""Solution for Advent of Code 2015, Day 17, Part 2."""

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


def part_two(document: str, target: int = 150) -> int:
    """Count exact-fit combinations using the fewest containers."""
    containers = parse_containers(document)

    @lru_cache(maxsize=None)
    def best(index: int, remaining: int) -> tuple[int, int]:
        if remaining == 0:
            return 0, 1
        if index == len(containers) or remaining < 0:
            return len(containers) + 1, 0

        skipped_count, skipped_ways = best(index + 1, remaining)
        used_count, used_ways = best(index + 1, remaining - containers[index])
        used_count += 1
        if skipped_count < used_count:
            return skipped_count, skipped_ways
        if used_count < skipped_count:
            return used_count, used_ways
        return skipped_count, skipped_ways + used_ways

    return best(0, target)[1]


if __name__ == "__main__":
    with open("inputs/2015/17.txt", encoding="utf-8") as input_file:
        print(part_two(input_file.read()))
