"""Solution for Advent of Code 2015, Day 20, Part 1."""


def target_presents(document: str) -> int:
    """Read the required present count."""
    values = document.split()
    if len(values) != 1 or not values[0].isdigit() or int(values[0]) <= 0:
        raise ValueError("expected one positive target")
    return int(values[0])


def part_one(document: str) -> int:
    """Return the first house receiving at least the target presents."""
    target = target_presents(document)
    limit = target // 10 + 1
    presents = [0] * limit
    for elf in range(1, limit):
        for house in range(elf, limit, elf):
            presents[house] += 10 * elf
    for house, total in enumerate(presents):
        if house and total >= target:
            return house
    raise AssertionError("sieve bound was insufficient")


if __name__ == "__main__":
    with open("inputs/2015/20.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
