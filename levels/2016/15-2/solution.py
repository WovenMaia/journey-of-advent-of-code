"""Solution for Advent of Code 2016, Day 15, Part 2."""

import re
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "15.txt"
LINE = re.compile(r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)\.")


def parse(text: str) -> list[tuple[int, int, int]]:
    """Parse discs as (number, positions, initial position)."""
    discs = []
    for line in text.splitlines():
        match = LINE.fullmatch(line.strip())
        if not match:
            raise ValueError(f"invalid disc: {line!r}")
        discs.append(tuple(map(int, match.groups())))
    if not discs:
        raise ValueError("no discs")
    return discs


def first_time(discs: list[tuple[int, int, int]]) -> int:
    """Return the first button time when every slot is aligned."""
    time = 0
    while True:
        if all((position + time + number) % positions == 0 for number, positions, position in discs):
            return time
        time += 1


def run(text: str) -> dict[str, int]:
    """Solve the puzzle after adding the seventh disc from Part 2."""
    discs = parse(text)
    extra_number = len(discs) + 1
    discs.append((extra_number, 11, 0))
    return {"a": first_time(discs)}


def main() -> int:
    print(run(INPUT_PATH.read_text(encoding="utf-8"))["a"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
