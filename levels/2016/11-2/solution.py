"""Solution for Advent of Code 2016, Day 11, Part 2."""

from collections import deque
from itertools import combinations
from pathlib import Path
import re

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "11.txt"
FLOORS = 4


def parse(text: str, extra_pairs: int = 2) -> tuple[int, tuple[tuple[int, int], ...]]:
    names: dict[str, int] = {}
    pairs: dict[int, list[int | None]] = {}
    for floor, line in enumerate(text.splitlines()):
        for name, kind in re.findall(r"(\w+)( generator|-compatible microchip)", line):
            index = names.setdefault(name, len(names))
            pair = pairs.setdefault(index, [None, None])
            pair[0 if kind == " generator" else 1] = floor
    if not pairs or any(None in pair for pair in pairs.values()):
        raise ValueError("incomplete component pair")
    return 0, tuple(sorted([(int(gen), int(chip)) for gen, chip in pairs.values()] + [(0, 0)] * extra_pairs))


def safe(pairs: tuple[tuple[int, int], ...]) -> bool:
    generators = {generator for generator, _ in pairs}
    return all(generator == chip or chip not in generators for generator, chip in pairs)


def minimum_steps(text: str) -> int:
    initial = parse(text)
    queue = deque([(initial, 0)])
    seen = {initial}
    while queue:
        (elevator, pairs), steps = queue.popleft()
        if all(generator == 3 and chip == 3 for generator, chip in pairs):
            return steps
        items = [(index, part) for index, (generator, chip) in enumerate(pairs) for part, floor in ((0, generator), (1, chip)) if floor == elevator]
        directions = (1, -1) if any(floor < elevator for generator, chip in pairs for floor in (generator, chip)) else (1,)
        for direction in directions:
            destination = elevator + direction
            if not 0 <= destination < FLOORS:
                continue
            for carried in combinations(items, 1):
                moved = [list(pair) for pair in pairs]
                for index, part in carried:
                    moved[index][part] = destination
                candidate = (destination, tuple(sorted((gen, chip) for gen, chip in moved)))
                if safe(candidate[1]) and candidate not in seen:
                    seen.add(candidate)
                    queue.append((candidate, steps + 1))
            for carried in combinations(items, 2):
                moved = [list(pair) for pair in pairs]
                for index, part in carried:
                    moved[index][part] = destination
                candidate = (destination, tuple(sorted((gen, chip) for gen, chip in moved)))
                if safe(candidate[1]) and candidate not in seen:
                    seen.add(candidate)
                    queue.append((candidate, steps + 1))
    raise ValueError("goal is unreachable")


def main() -> int:
    print(minimum_steps(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
