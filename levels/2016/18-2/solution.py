"""Solution for Advent of Code 2016, Day 18, Part 2."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "18.txt"
ROWS = 400_000


def safe_tiles(first_row: str, rows: int) -> int:
    """Count safe tiles in the requested number of rows."""
    row = first_row.strip()
    if not row or any(tile not in ".^" for tile in row):
        raise ValueError("row must contain only . and ^")
    if rows < 1:
        raise ValueError("rows must be positive")
    total = 0
    for _ in range(rows):
        total += row.count(".")
        padded = "." + row + "."
        row = "".join("^" if padded[index] != padded[index + 2] else "." for index in range(len(row)))
    return total


def main() -> int:
    print(safe_tiles(INPUT_PATH.read_text(encoding="utf-8"), ROWS))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
