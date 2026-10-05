"""Solution for Advent of Code 2016, Day 6, Part 2."""

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
    """Choose the least frequent character from each signal column."""
    rows = messages(text)
    result = []
    for column in zip(*rows):
        counts = Counter(column)
        result.append(min(counts, key=lambda char: (counts[char], char)))
    return "".join(result)


def main() -> int:
    print(decode(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
