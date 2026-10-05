"""Solution for Advent of Code 2016, Day 19, Part 1."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "19.txt"


def winner(elf_count: int) -> int:
    """Return the winning elf when each elf steals from the next elf."""
    if elf_count < 1:
        raise ValueError("elf count must be positive")
    power = 1 << (elf_count.bit_length() - 1)
    return 2 * (elf_count - power) + 1


def main() -> int:
    print(winner(int(INPUT_PATH.read_text(encoding="utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
