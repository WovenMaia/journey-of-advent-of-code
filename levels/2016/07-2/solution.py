"""Solution for Advent of Code 2016, Day 7, Part 2."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "07.txt"


def parse_address(address: str) -> tuple[list[str], list[str]]:
    """Split an address into supernet and hypernet sequences."""
    pieces = address.replace("]", "[").split("[")
    if len(pieces) % 2 == 0 or not pieces or any(not piece for piece in pieces):
        raise ValueError(f"invalid address: {address!r}")
    return pieces[::2], pieces[1::2]


def abas(sequence: str) -> set[str]:
    """Return ABA motifs from a sequence."""
    return {a + b + a for a, b, c in zip(sequence, sequence[1:], sequence[2:]) if a == c and a != b}


def supports_ssl(address: str) -> bool:
    """Return whether an outside ABA has its corresponding inside BAB."""
    supernets, hypernets = parse_address(address)
    wanted = {motif[1] + motif[0] + motif[1] for sequence in supernets for motif in abas(sequence)}
    return any(wanted.intersection(abas(sequence)) for sequence in hypernets)


def count_ssl(text: str) -> int:
    return sum(supports_ssl(line.strip()) for line in text.splitlines() if line.strip())


def main() -> int:
    print(count_ssl(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
