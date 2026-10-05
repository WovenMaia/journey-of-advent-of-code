"""Solution for Advent of Code 2016, Day 7, Part 1."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "07.txt"


def parse_address(address: str) -> tuple[list[str], list[str]]:
    """Split an address into supernet and hypernet sequences."""
    pieces = address.replace("]", "[").split("[")
    if len(pieces) % 2 == 0 or not pieces or any(not piece for piece in pieces):
        raise ValueError(f"invalid address: {address!r}")
    return pieces[::2], pieces[1::2]


def has_abba(sequence: str) -> bool:
    """Return whether sequence contains a four-character ABBA."""
    return any(a != b and a == d and b == c for a, b, c, d in zip(sequence, sequence[1:], sequence[2:], sequence[3:]))


def supports_tls(address: str) -> bool:
    """Return whether address has an outside ABBA and no inside ABBA."""
    supernets, hypernets = parse_address(address)
    return any(has_abba(sequence) for sequence in supernets) and not any(has_abba(sequence) for sequence in hypernets)


def count_tls(text: str) -> int:
    return sum(supports_tls(line.strip()) for line in text.splitlines() if line.strip())


def main() -> int:
    print(count_tls(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
