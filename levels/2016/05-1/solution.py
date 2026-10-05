"""Solution for Advent of Code 2016, Day 5, Part 1."""

import hashlib
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "05.txt"


def password(door_id: str, *, length: int = 8, max_index: int | None = None) -> str:
    """Find the password by accepting the sixth hex digit of qualifying MD5 hashes."""
    if not door_id or length < 1:
        raise ValueError("door ID and positive length are required")
    found: list[str] = []
    index = 0
    while len(found) < length:
        if max_index is not None and index >= max_index:
            raise ValueError(f"search exceeded index limit {max_index}")
        digest = hashlib.md5(f"{door_id}{index}".encode("ascii")).hexdigest()
        if digest.startswith("00000"):
            found.append(digest[5])
        index += 1
    return "".join(found)


def main() -> int:
    print(password(INPUT_PATH.read_text(encoding="utf-8").strip()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
