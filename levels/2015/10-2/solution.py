"""Solution for Advent of Code 2015, Day 10, Part 2."""

from itertools import groupby


def look_and_say(sequence: str, repetitions: int) -> str:
    """Apply the look-and-say transformation the requested number of times."""
    if not sequence or not sequence.isdigit():
        raise ValueError("sequence must contain at least one digit")
    if repetitions < 0:
        raise ValueError("repetitions must not be negative")

    for _ in range(repetitions):
        sequence = "".join(
            f"{sum(1 for _ in run)}{digit}"
            for digit, run in groupby(sequence)
        )
    return sequence


def result_length(sequence: str, repetitions: int) -> int:
    """Return the length after repeatedly applying look-and-say."""
    return len(look_and_say(sequence, repetitions))


if __name__ == "__main__":
    with open("inputs/2015/10.txt", encoding="utf-8") as input_file:
        print(result_length(input_file.read().strip(), 50))
