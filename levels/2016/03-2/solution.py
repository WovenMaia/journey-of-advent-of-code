"""Solution for Advent of Code 2016, Day 3, Part 2."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "03.txt"


def parse_rows(text: str) -> list[tuple[int, int, int]]:
    """Parse one triple of side lengths from each non-empty line."""
    rows: list[tuple[int, int, int]] = []
    for raw in text.splitlines():
        values = raw.split()
        if not values:
            continue
        if len(values) != 3 or any(not value.isdigit() for value in values):
            raise ValueError(f"invalid triangle row: {raw!r}")
        rows.append(tuple(int(value) for value in values))
    if len(rows) % 3:
        raise ValueError("triangle rows must be grouped in threes")
    return rows


def is_valid(sides: tuple[int, int, int]) -> bool:
    """Return whether three side lengths can form a triangle."""
    a, b, c = sorted(sides)
    return a + b > c


def count_valid(text: str) -> int:
    """Count valid triangles by reading each group vertically by columns."""
    rows = parse_rows(text)
    total = 0
    for start in range(0, len(rows), 3):
        group = rows[start : start + 3]
        total += sum(is_valid(tuple(row[column] for row in group)) for column in range(3))
    return total


def main() -> int:
    print(count_valid(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
