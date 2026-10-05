"""Solution for Advent of Code 2016, Day 21, Part 1."""

from pathlib import Path
import re

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "21.txt"


def _rotate(value: list[str], amount: int) -> None:
    amount %= len(value)
    if amount:
        value[:] = value[-amount:] + value[:-amount]


def scramble(text: str, password: str = "abcdefgh") -> str:
    """Apply the scrambling instructions to a password."""
    value = list(password)
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        match = re.fullmatch(r"swap position (\d+) with position (\d+)", line)
        if match:
            left, right = map(int, match.groups())
            value[left], value[right] = value[right], value[left]
            continue
        match = re.fullmatch(r"swap letter ([a-z]) with letter ([a-z])", line)
        if match:
            left, right = match.groups()
            value = [right if char == left else left if char == right else char for char in value]
            continue
        match = re.fullmatch(r"rotate (left|right) (\d+) step(?:s)?", line)
        if match:
            direction, amount = match.groups()
            amount = int(amount) * (1 if direction == "right" else -1)
            _rotate(value, amount)
            continue
        match = re.fullmatch(r"rotate based on position of letter ([a-z])", line)
        if match:
            index = value.index(match.group(1))
            _rotate(value, index + 1 + (index >= 4))
            continue
        match = re.fullmatch(r"reverse positions (\d+) through (\d+)", line)
        if match:
            left, right = map(int, match.groups())
            value[left : right + 1] = reversed(value[left : right + 1])
            continue
        match = re.fullmatch(r"move position (\d+) to position (\d+)", line)
        if match:
            left, right = map(int, match.groups())
            char = value.pop(left)
            value.insert(right, char)
            continue
        raise ValueError(f"unrecognized instruction: {line}")
    return "".join(value)


def run(text: str) -> dict[str, str]:
    return {"a": scramble(text)}


def main() -> int:
    print(scramble(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
