"""Solution for Advent of Code 2015, Day 16, Part 2."""

from dataclasses import dataclass
import re


TARGETS = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
_GREATER_THAN = frozenset(("cats", "trees"))
_LESS_THAN = frozenset(("pomeranians", "goldfish"))
_LINE = re.compile(r"^Sue (\d+): (.+)$")
_PROPERTY = re.compile(r"^(\w+): (-?\d+)$")


@dataclass(frozen=True)
class Sue:
    """One candidate's observed compound quantities."""

    number: int
    compounds: tuple[tuple[str, int], ...]


def parse_sues(document: str) -> tuple[Sue, ...]:
    """Parse candidate descriptions from the puzzle input."""
    sues: list[Sue] = []
    for line in document.splitlines():
        if not line:
            continue
        match = _LINE.fullmatch(line)
        if match is None:
            raise ValueError(f"invalid Sue description: {line!r}")
        number, observations = match.groups()
        compounds: list[tuple[str, int]] = []
        seen: set[str] = set()
        for observation in observations.split(", "):
            property_match = _PROPERTY.fullmatch(observation)
            if property_match is None:
                raise ValueError(f"invalid observation: {observation!r}")
            compound, quantity = property_match.groups()
            if compound not in TARGETS:
                raise ValueError(f"unknown compound: {compound!r}")
            if compound in seen:
                raise ValueError(f"duplicate compound: {compound!r}")
            seen.add(compound)
            compounds.append((compound, int(quantity)))
        sues.append(Sue(int(number), tuple(compounds)))
    return tuple(sues)


def _matches(compound: str, quantity: int) -> bool:
    target = TARGETS[compound]
    if compound in _GREATER_THAN:
        return quantity > target
    if compound in _LESS_THAN:
        return quantity < target
    return quantity == target


def part_two(document: str) -> int:
    """Return the number of the sole candidate matching Part 2 rules."""
    matches = [
        sue.number
        for sue in parse_sues(document)
        if all(_matches(compound, quantity) for compound, quantity in sue.compounds)
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one matching Sue, found {len(matches)}")
    return matches[0]


if __name__ == "__main__":
    with open("inputs/2015/16.txt", encoding="utf-8") as input_file:
        print(part_two(input_file.read()))
