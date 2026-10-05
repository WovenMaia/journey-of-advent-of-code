"""Solution for Advent of Code 2016, Day 13, Part 2."""

from collections import deque
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "13.txt"
START = (1, 1)
LIMIT = 50


def is_open(favorite: int, x: int, y: int) -> bool:
    """Return whether a non-negative coordinate is an open space."""
    if x < 0 or y < 0:
        return False
    value = x * x + 3 * x + 2 * x * y + y + y * y + favorite
    return value.bit_count() % 2 == 0


def reachable(favorite: int, limit: int = LIMIT) -> set[tuple[int, int]]:
    """Return coordinates reachable in at most limit steps."""
    queue = deque([(START, 0)])
    seen = {START}
    while queue:
        (x, y), distance = queue.popleft()
        if distance == limit:
            continue
        for neighbor in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if neighbor not in seen and is_open(favorite, *neighbor):
                seen.add(neighbor)
                queue.append((neighbor, distance + 1))
    return seen


def run(text: str) -> dict[str, int]:
    """Solve the puzzle for the supplied favorite number."""
    return {"a": len(reachable(int(text.strip())))}


def main() -> int:
    print(run(INPUT_PATH.read_text(encoding="utf-8"))["a"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
