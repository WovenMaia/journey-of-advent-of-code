"""Solution for Advent of Code 2015, Day 14, Part 1."""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Reindeer:
    """A reindeer's speed and repeating flight/rest schedule."""

    name: str
    speed: int
    flight_seconds: int
    rest_seconds: int


_LINE = re.compile(
    r"^(\w+) can fly (\d+) km/s for (\d+) seconds, "
    r"but then must rest for (\d+) seconds\.$"
)


def parse_reindeer(document: str) -> tuple[Reindeer, ...]:
    """Parse reindeer descriptions from the puzzle input."""
    reindeer: list[Reindeer] = []
    for line in document.splitlines():
        if not line:
            continue
        match = _LINE.fullmatch(line)
        if match is None:
            raise ValueError(f"invalid reindeer description: {line!r}")
        name, speed, flight_seconds, rest_seconds = match.groups()
        reindeer.append(
            Reindeer(name, int(speed), int(flight_seconds), int(rest_seconds))
        )
    return tuple(reindeer)


def distance_after(reindeer: Reindeer, seconds: int) -> int:
    """Return the distance travelled by one reindeer after ``seconds`` seconds."""
    if seconds < 0:
        raise ValueError("seconds must not be negative")
    cycle_seconds = reindeer.flight_seconds + reindeer.rest_seconds
    full_cycles, remaining = divmod(seconds, cycle_seconds)
    flying_seconds = full_cycles * reindeer.flight_seconds + min(
        remaining, reindeer.flight_seconds
    )
    return reindeer.speed * flying_seconds


def part_one(document: str, seconds: int = 2503) -> int:
    """Return the greatest distance travelled after the race duration."""
    return max(
        (distance_after(reindeer, seconds) for reindeer in parse_reindeer(document)),
        default=0,
    )


if __name__ == "__main__":
    with open("inputs/2015/14.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
