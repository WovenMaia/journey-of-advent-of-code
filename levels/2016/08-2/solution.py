"""Solution for Advent of Code 2016, Day 8, Part 2."""

import re
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "08.txt"
COMMAND = re.compile(r"(?:rect (\d+)x(\d+)|rotate row y=(\d+) by (\d+)|rotate column x=(\d+) by (\d+))$")


def run(text: str, width: int = 50, height: int = 6) -> list[list[bool]]:
    screen = [[False] * width for _ in range(height)]
    for raw in text.splitlines():
        line = raw.strip()
        if not line: continue
        match = COMMAND.fullmatch(line)
        if not match: raise ValueError(f"invalid command: {line!r}")
        rect_w, rect_h, row, row_by, column, column_by = (int(value) if value else None for value in match.groups())
        if rect_w is not None:
            if rect_w > width or rect_h > height: raise ValueError("rectangle exceeds screen")
            for y in range(rect_h):
                for x in range(rect_w): screen[y][x] = True
        elif row is not None:
            if row >= height: raise ValueError("row exceeds screen")
            shift = row_by % width
            screen[row] = screen[row][-shift:] + screen[row][:-shift] if shift else screen[row][:]
        else:
            if column >= width: raise ValueError("column exceeds screen")
            shift = column_by % height
            values = [screen[y][column] for y in range(height)]
            values = values[-shift:] + values[:-shift] if shift else values
            for y, value in enumerate(values): screen[y][column] = value
    return screen


def render(screen: list[list[bool]]) -> str:
    return "\n".join("".join("#" if pixel else "." for pixel in row) for row in screen)

def code(text: str, width: int = 50, height: int = 6) -> str:
    """Render the final display; read the letter code from this six-row bitmap."""
    return render(run(text, width, height))


def main() -> int:
    print(code(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
