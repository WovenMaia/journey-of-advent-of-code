"""Solution for Advent of Code 2016, Day 24, Part 2."""

from collections import deque
from itertools import permutations
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "24.txt"


def _distances(text: str) -> dict[str, dict[str, int]]:
    grid = [list(line) for line in text.splitlines() if line]
    points = {
        char: (x, y)
        for y, row in enumerate(grid)
        for x, char in enumerate(row)
        if char.isdigit()
    }
    if "0" not in points:
        raise ValueError("map has no starting point")
    distances = {label: {} for label in points}
    for source, (sx, sy) in points.items():
        queue = deque([((sx, sy), 0)])
        seen = {(sx, sy)}
        while queue:
            (x, y), distance = queue.popleft()
            if grid[y][x].isdigit():
                distances[source][grid[y][x]] = distance
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] != "#" and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    queue.append(((nx, ny), distance + 1))
    return distances


def shortest_route(text: str) -> int:
    distances = _distances(text)
    targets = sorted(label for label in distances if label != "0")
    return min(
        sum(distances[left][right] for left, right in zip(("0",) + order, order + ("0",)))
        for order in permutations(targets)
    )


def run(text: str) -> dict[str, int]:
    return {"a": shortest_route(text)}


def main() -> int:
    print(shortest_route(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
