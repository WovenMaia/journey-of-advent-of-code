"""Solution for Advent of Code 2016, Day 2, Part 2."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "02.txt"


def parse_instructions(text: str) -> list[str]:
    """Return non-empty keypad instruction lines after validating their moves."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    for line in lines:
        if any(move not in "UDLR" for move in line):
            raise ValueError(f"invalid move line: {line!r}")
    return lines


def code(text: str) -> str:
    """Return the bathroom code for the diamond-shaped keypad."""
    keypad = {
        (2, 0): "1",
        (1, 1): "2", (2, 1): "3", (3, 1): "4",
        (0, 2): "5", (1, 2): "6", (2, 2): "7", (3, 2): "8", (4, 2): "9",
        (1, 3): "A", (2, 3): "B", (3, 3): "C",
        (2, 4): "D",
    }
    moves = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    x, y = 0, 2
    digits: list[str] = []
    for line in parse_instructions(text):
        for move in line:
            dx, dy = moves[move]
            candidate = (x + dx, y + dy)
            if candidate in keypad:
                x, y = candidate
        digits.append(keypad[(x, y)])
    return "".join(digits)


def main() -> int:
    print(code(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
