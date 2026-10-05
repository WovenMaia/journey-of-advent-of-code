"""Solution for Advent of Code 2016, Day 13, Part 1."""

from collections import deque
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "13.txt"
START = (1, 1)
TARGET = (31, 39)


def is_open(favorite: int, x: int, y: int) -> bool:
    """Return whether a non-negative coordinate is an open space."""
    if x < 0 or y < 0:
        return False
    value = x * x + 3 * x + 2 * x * y + y + y * y + favorite
    return value.bit_count() % 2 == 0


def shortest_path(favorite: int, target: tuple[int, int] = TARGET) -> int:
    """Find the shortest route from (1, 1) to target with BFS."""
    queue = deque([(START, 0)])
    seen = {START}
    while queue:
        (x, y), distance = queue.popleft()
        if (x, y) == target:
            return distance
        for neighbor in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if neighbor not in seen and is_open(favorite, *neighbor):
                seen.add(neighbor)
                queue.append((neighbor, distance + 1))
    raise ValueError("target is unreachable")


def run(text: str) -> dict[str, int]:
    """Solve the puzzle for the supplied favorite number."""
    return {"a": shortest_path(int(text.strip()))}


def main() -> int:
    print(run(INPUT_PATH.read_text(encoding="utf-8"))["a"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
