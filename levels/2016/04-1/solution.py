"""Solution for Advent of Code 2016, Day 4, Part 1."""

from collections import Counter
from pathlib import Path
import re

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "04.txt"
ROOM_PATTERN = re.compile(r"^(?P<name>[a-z-]+)-(?P<sector>\d+)\[(?P<checksum>[a-z]{5})\]$")


def parse_rooms(text: str) -> list[tuple[str, int, str]]:
    """Parse encrypted room names, sector IDs, and checksums."""
    rooms: list[tuple[str, int, str]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        match = ROOM_PATTERN.fullmatch(line)
        if not match:
            raise ValueError(f"invalid room: {raw!r}")
        rooms.append((match["name"], int(match["sector"]), match["checksum"]))
    return rooms


def is_real(name: str, checksum: str) -> bool:
    """Return whether checksum matches frequency then alphabetic order."""
    counts = Counter(name.replace("-", ""))
    expected = "".join(sorted(counts, key=lambda letter: (-counts[letter], letter))[:5])
    return expected == checksum


def sector_sum(text: str) -> int:
    """Sum sector IDs of rooms with valid checksums."""
    return sum(sector for name, sector, checksum in parse_rooms(text) if is_real(name, checksum))


def main() -> int:
    print(sector_sum(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
