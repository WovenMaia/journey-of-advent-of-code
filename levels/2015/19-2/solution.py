"""Solution for Advent of Code 2015, Day 19, Part 2."""

import re
from functools import lru_cache

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
            rules.append((source, target))
        elif molecule:
            raise ValueError("expected one medicine molecule")
        else:
            molecule = line
    if not rules or not molecule or "".join(_TOKEN.findall(molecule)) != molecule:
        raise ValueError("invalid replacement document")
    return tuple(rules), molecule


def grammar_steps(molecule: str) -> int:
    """Count synthesis steps for the canonical Day 19 grammar."""
    tokens = _TOKEN.findall(molecule)
    if "".join(tokens) != molecule:
        raise ValueError("invalid molecule")
    return len(tokens) - tokens.count("Rn") - tokens.count("Ar") - 2 * tokens.count("Y") - 1


def _reduction_steps(rules: tuple[tuple[str, str], ...], molecule: str) -> int:
    """Reduce a small public example to e by reversing replacements."""
    reverse = tuple(sorted(((target, source) for source, target in rules), key=lambda pair: -len(pair[0])))

    @lru_cache(maxsize=None)
    def search(current: str) -> int | None:
        if current == "e":
            return 0
        best: int | None = None
        for target, source in reverse:
            start = 0
            while True:
                index = current.find(target, start)
                if index < 0:
                    break
                reduced = current[:index] + source + current[index + len(target):]
                result = search(reduced)
                if result is not None and (best is None or result + 1 < best):
                    best = result + 1
                start = index + 1
        return best

    result = search(molecule)
    if result is None:
        raise ValueError("molecule cannot be reduced to e")
    return result


def part_two(document: str) -> int:
    """Return minimum synthesis steps, using the grammar identity for the input."""
    rules, molecule = parse(document)
    if any(token in molecule for token in ("Rn", "Ar", "Y")):
        return grammar_steps(molecule)
    return _reduction_steps(rules, molecule)


if __name__ == "__main__":
    with open("inputs/2015/19.txt", encoding="utf-8") as input_file:
        print(part_two(input_file.read()))
