"""Solution for Advent of Code 2016, Day 5, Part 2."""

import hashlib
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "05.txt"


def password(door_id: str, *, length: int = 8, max_index: int | None = None) -> str:
    """Fill password positions from qualifying MD5 hashes in index order."""
    if not door_id or length < 1:
        raise ValueError("door ID and positive length are required")
    found: list[str | None] = [None] * length
    remaining = length
    index = 0
    while remaining:
        if max_index is not None and index >= max_index:
            raise ValueError(f"search exceeded index limit {max_index}")
        digest = hashlib.md5(f"{door_id}{index}".encode("ascii")).hexdigest()
        if digest.startswith("00000"):
            position = digest[5]
            if position.isdigit() and int(position) < length and found[int(position)] is None:
                found[int(position)] = digest[6]
                remaining -= 1
        index += 1
    return "".join(character or "_" for character in found)


def main() -> int:
    print(password(INPUT_PATH.read_text(encoding="utf-8").strip()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
