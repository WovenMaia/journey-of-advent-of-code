"""Solution for Advent of Code 2016, Day 9, Part 2."""

import re
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "09.txt"
MARKER = re.compile(r"\((\d+)x(\d+)\)")


def decompressed_length(text: str) -> int:
    """Return the recursively decompressed length without materializing output."""
    data = "".join(text.split())

    def length(start: int, end: int) -> int:
        total = 0
        cursor = start
        while cursor < end:
            if data[cursor] != "(":
                total += 1
                cursor += 1
                continue
            marker = MARKER.match(data, cursor)
            if marker is None:
                raise ValueError(f"invalid marker at offset {cursor}")
            size, repeats = (int(value) for value in marker.groups())
            section_start = marker.end()
            section_end = section_start + size
            if section_end > end:
                raise ValueError("marker exceeds input")
            total += repeats * length(section_start, section_end)
            cursor = section_end
        return total

    return length(0, len(data))


def main() -> int:
    print(decompressed_length(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
