"""Solution for Advent of Code 2016, Day 16, Part 1."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "16.txt"
DISK_SIZE = 272


def dragon_step(data: str) -> str:
    """Expand one dragon-curve step."""
    inverted = "".join("1" if bit == "0" else "0" for bit in reversed(data))
    return f"{data}0{inverted}"


def fill(initial: str, size: int) -> str:
    """Generate enough dragon-curve data and truncate to the disk size."""
    data = initial.strip()
    if not data or any(bit not in "01" for bit in data):
        raise ValueError("initial data must be a non-empty bit string")
    while len(data) < size:
        data = dragon_step(data)
    return data[:size]


def checksum(data: str) -> str:
    """Reduce pairs until the checksum length is odd."""
    while len(data) % 2 == 0:
        data = "".join("1" if left == right else "0" for left, right in zip(data[::2], data[1::2]))
    return data


def run(text: str) -> dict[str, str]:
    """Solve the puzzle for the fixed Part 1 disk size."""
    return {"a": checksum(fill(text, DISK_SIZE))}


def main() -> int:
    print(run(INPUT_PATH.read_text(encoding="utf-8"))["a"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
