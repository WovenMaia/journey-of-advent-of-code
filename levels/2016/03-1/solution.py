"""Solution for Advent of Code 2016, Day 3, Part 1."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "03.txt"


def parse_triangles(text: str) -> list[tuple[int, int, int]]:
    """Parse one triple of side lengths from each non-empty line."""
    triangles: list[tuple[int, int, int]] = []
    for raw in text.splitlines():
        values = raw.split()
        if not values:
            continue
        if len(values) != 3 or any(not value.isdigit() for value in values):
            raise ValueError(f"invalid triangle row: {raw!r}")
        triangles.append(tuple(int(value) for value in values))
    return triangles


def is_valid(sides: tuple[int, int, int]) -> bool:
    """Return whether three side lengths can form a triangle."""
    a, b, c = sorted(sides)
    return a + b > c


def count_valid(text: str) -> int:
    """Count valid triangles listed row by row."""
    return sum(is_valid(sides) for sides in parse_triangles(text))


def main() -> int:
    print(count_valid(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
