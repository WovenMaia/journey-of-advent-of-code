"""Solution for Advent of Code 2016, Day 17, Part 2."""

from collections import deque
import hashlib
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "17.txt"
DIRECTIONS = ((0, -1, "U"), (0, 1, "D"), (-1, 0, "L"), (1, 0, "R"))


def longest_path_length(passcode: str) -> int:
    """Return the length of the longest path that reaches the vault."""
    passcode = passcode.strip()
    if not passcode:
        raise ValueError("passcode must not be empty")
    queue = deque([(0, 0, "")])
    longest = 0
    while queue:
        x, y, path = queue.popleft()
        if (x, y) == (3, 3):
            longest = max(longest, len(path))
            continue
        doors = hashlib.md5((passcode + path).encode(), usedforsecurity=False).hexdigest()[:4]
        for (dx, dy, step), state in zip(DIRECTIONS, doors):
            nx, ny = x + dx, y + dy
            if state in "bcdef" and 0 <= nx < 4 and 0 <= ny < 4:
                queue.append((nx, ny, path + step))
    return longest


def main() -> int:
    print(longest_path_length(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
