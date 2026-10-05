"""Solution for Advent of Code 2015, Day 13, Part 1."""

from itertools import permutations


def parse_preferences(document: str) -> dict[str, dict[str, int]]:
    """Parse each directed neighbour preference from the puzzle input."""
    preferences: dict[str, dict[str, int]] = {}
    for line in document.splitlines():
        words = line.rstrip(".").split()
        if not words:
            continue
        guest, direction, amount, neighbour = (
            words[0],
            words[2],
            int(words[3]),
            words[-1],
        )
        if direction == "lose":
            amount = -amount
        preferences.setdefault(guest, {})[neighbour] = amount
    return preferences


def total_happiness(
    seating: tuple[str, ...], preferences: dict[str, dict[str, int]]
) -> int:
    """Return the circular table's combined directed happiness change."""
    return sum(
        preferences[guest][neighbour] + preferences[neighbour][guest]
        for guest, neighbour in zip(seating, seating[1:] + seating[:1])
    )


def part_one(document: str) -> int:
    """Return the maximum happiness over all circular seating arrangements."""
    preferences = parse_preferences(document)
    guests = sorted(preferences)
    if not guests:
        return 0
    anchor, *remaining = guests
    return max(
        total_happiness((anchor, *arrangement), preferences)
        for arrangement in permutations(remaining)
    )


if __name__ == "__main__":
    with open("inputs/2015/13.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
