"""Solution for Advent of Code 2016, Day 1, Part 2."""

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


def first_revisited(text: str) -> tuple[int, int]:
    """Return the first coordinate visited twice, one block at a time."""
    x = y = direction = 0
    headings = ((0, 1), (1, 0), (0, -1), (-1, 0))
    visited = {(0, 0)}
    for turn, distance in parse_instructions(text):
        direction = (direction + (1 if turn == "R" else -1)) % 4
        dx, dy = headings[direction]
        for _ in range(distance):
            x += dx
            y += dy
            if (x, y) in visited:
                return x, y
            visited.add((x, y))
    raise ValueError("route never visits a location twice")


def distance(text: str) -> int:
    """Return the Manhattan distance to the first revisited location."""
    x, y = first_revisited(text)
    return abs(x) + abs(y)


def main() -> int:
    print(distance(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
