"""Solution for Advent of Code 2016, Day 1, Part 1."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "01.txt"


def parse_instructions(text: str) -> list[tuple[str, int]]:
    """Parse comma-separated turns and distances."""
    instructions: list[tuple[str, int]] = []
    for raw in text.split(","):
        token = raw.strip()
        if len(token) < 2 or token[0] not in "LR" or not token[1:].isdigit():
            raise ValueError(f"invalid instruction: {token!r}")
        instructions.append((token[0], int(token[1:])))
    return instructions


def destination(text: str) -> tuple[int, int]:
    """Return the final east/north coordinates after following every turn."""
    x = y = direction = 0
    headings = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for turn, distance in parse_instructions(text):
        direction = (direction + (1 if turn == "R" else -1)) % 4
        dx, dy = headings[direction]
        x += dx * distance
        y += dy * distance
    return x, y


def distance(text: str) -> int:
    """Return the Manhattan distance from the starting intersection."""
    x, y = destination(text)
    return abs(x) + abs(y)


def main() -> int:
    print(distance(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
