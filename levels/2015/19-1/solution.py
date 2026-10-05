"""Solution for Advent of Code 2015, Day 19, Part 1."""

import re

_TOKEN = re.compile(r"[A-Z][a-z]?")


def parse(document: str) -> tuple[tuple[tuple[str, str], ...], str]:
    """Parse replacement rules and the medicine molecule."""
    rules: list[tuple[str, str]] = []
    molecule = ""
    for line in document.splitlines():
        if not line:
            continue
        if " => " in line:
            source, target = line.split(" => ", 1)
            if not source or not target:
                raise ValueError(f"invalid replacement: {line!r}")
            rules.append((source, target))
        else:
            if molecule:
                raise ValueError("expected one medicine molecule")
            molecule = line
    if not rules or not molecule or "".join(_TOKEN.findall(molecule)) != molecule:
        raise ValueError("invalid replacement document")
    return tuple(rules), molecule


def part_one(document: str) -> int:
    """Count distinct molecules reachable with one replacement."""
    rules, molecule = parse(document)
    generated: set[str] = set()
    for source, target in rules:
        start = 0
        while True:
            position = molecule.find(source, start)
            if position < 0:
                break
            generated.add(molecule[:position] + target + molecule[position + len(source):])
            start = position + 1
    return len(generated)


if __name__ == "__main__":
    with open("inputs/2015/19.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
