"""Solution for Advent of Code 2016, Day 6, Part 1."""

from collections import Counter
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "06.txt"


def messages(text: str) -> list[str]:
    """Return non-empty signal rows and require a rectangular recording."""
    rows = [line.strip() for line in text.splitlines() if line.strip()]
    if not rows or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("signal must be a non-empty rectangle")
    return rows


def decode(text: str) -> str:
    """Choose the most frequent character from each signal column."""
    rows = messages(text)
    return "".join(min(Counter(column), key=lambda char: (-Counter(column)[char], char)) for column in zip(*rows))


def main() -> int:
    print(decode(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
