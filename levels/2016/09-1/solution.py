"""Solution for Advent of Code 2016, Day 9, Part 1."""

import re
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "09.txt"
MARKER = re.compile(r"\((\d+)x(\d+)\)")


def decompressed_length(text: str) -> int:
    """Return the length after one-level marker expansion."""
    data = "".join(text.split())
    length = 0
    cursor = 0
    while cursor < len(data):
        if data[cursor] != "(":
            length += 1
            cursor += 1
            continue
        marker = MARKER.match(data, cursor)
        if marker is None:
            raise ValueError(f"invalid marker at offset {cursor}")
        size, repeats = (int(value) for value in marker.groups())
        start = marker.end()
        end = start + size
        if end > len(data):
            raise ValueError("marker exceeds input")
        length += size * repeats
        cursor = end
    return length


def main() -> int:
    print(decompressed_length(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
