"""Solution for Advent of Code 2016, Day 20, Part 1."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "20.txt"
MAX_IP = 4_294_967_295


def parse_ranges(text: str) -> list[tuple[int, int]]:
    """Parse and validate inclusive blocked IP ranges."""
    ranges = []
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            left, right = (int(part) for part in line.strip().split("-"))
        except (ValueError, TypeError):
            raise ValueError("ranges must use low-high format") from None
        if left < 0 or right < left:
            raise ValueError("ranges must be non-negative and ordered")
        ranges.append((left, right))
    return ranges


def first_allowed(text: str, maximum: int = MAX_IP) -> int | None:
    """Return the smallest unblocked address in the inclusive address space."""
    if maximum < 0:
        raise ValueError("maximum must be non-negative")
    candidate = 0
    for low, high in sorted(parse_ranges(text)):
        if low > candidate:
            return candidate
        candidate = max(candidate, high + 1)
        if candidate > maximum:
            return None
    return candidate


def main() -> int:
    print(first_allowed(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
