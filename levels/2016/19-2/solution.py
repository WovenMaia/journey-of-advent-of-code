"""Solution for Advent of Code 2016, Day 19, Part 2."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "19.txt"


def winner(elf_count: int) -> int:
    """Return the winning elf when each elf steals across the circle."""
    if elf_count < 1:
        raise ValueError("elf count must be positive")
    power = 1
    while power * 3 <= elf_count:
        power *= 3
    remainder = elf_count - power
    if remainder == 0:
        return elf_count
    if remainder <= power:
        return remainder
    return 2 * remainder - power


def main() -> int:
    print(winner(int(INPUT_PATH.read_text(encoding="utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
