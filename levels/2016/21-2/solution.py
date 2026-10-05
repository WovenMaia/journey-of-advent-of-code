"""Solution for Advent of Code 2016, Day 21, Part 2."""

from pathlib import Path
import re

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "21.txt"


def _rotate(value: list[str], amount: int) -> None:
    amount %= len(value)
    if amount:
        value[:] = value[-amount:] + value[:-amount]


def _apply(value: list[str], line: str) -> None:
    match = re.fullmatch(r"swap position (\d+) with position (\d+)", line)
    if match:
        left, right = map(int, match.groups())
        value[left], value[right] = value[right], value[left]
        return
    match = re.fullmatch(r"swap letter ([a-z]) with letter ([a-z])", line)
    if match:
        left, right = match.groups()
        for index, char in enumerate(value):
            if char == left:
                value[index] = right
            elif char == right:
                value[index] = left
        return
    match = re.fullmatch(r"rotate (left|right) (\d+) step(?:s)?", line)
    if match:
        direction, amount = match.groups()
        _rotate(value, int(amount) * (1 if direction == "right" else -1))
        return
    match = re.fullmatch(r"rotate based on position of letter ([a-z])", line)
    if match:
        index = value.index(match.group(1))
        _rotate(value, index + 1 + (index >= 4))
        return
    match = re.fullmatch(r"reverse positions (\d+) through (\d+)", line)
    if match:
        left, right = map(int, match.groups())
        value[left : right + 1] = reversed(value[left : right + 1])
        return
    match = re.fullmatch(r"move position (\d+) to position (\d+)", line)
    if match:
        left, right = map(int, match.groups())
        value.insert(right, value.pop(left))
        return
    raise ValueError(f"unrecognized instruction: {line}")


def unscramble(text: str, password: str = "fbgdceah") -> str:
    """Reverse the scrambling instructions for a known scrambled password."""
    value = list(password)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    for line in reversed(lines):
        match = re.fullmatch(r"rotate based on position of letter ([a-z])", line)
        if match:
            target = match.group(1)
            original = None
            for amount in range(len(value)):
                candidate = value[:]
                _rotate(candidate, -amount)
                transformed = candidate[:]
                index = transformed.index(target)
                _rotate(transformed, index + 1 + (index >= 4))
                if transformed == value:
                    original = candidate
                    break
            if original is None:
                raise ValueError("rotate based instruction has no inverse")
            value = original
            continue
        match = re.fullmatch(r"rotate (left|right) (\d+) step(?:s)?", line)
        if match:
            direction, amount = match.groups()
            _rotate(value, int(amount) * (-1 if direction == "right" else 1))
            continue
        match = re.fullmatch(r"move position (\d+) to position (\d+)", line)
        if match:
            left, right = map(int, match.groups())
            value.insert(left, value.pop(right))
            continue
        _apply(value, line)
    return "".join(value)


def run(text: str) -> dict[str, str]:
    return {"a": unscramble(text)}


def main() -> int:
    print(unscramble(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
