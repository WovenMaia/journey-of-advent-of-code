"""Solution for Advent of Code 2015, Day 4, Part 2."""

from hashlib import md5


def lowest_adventcoin_number_with_six_zeroes(secret_key: str) -> int:
    """Return the lowest positive suffix whose MD5 hash starts with six zeroes."""
    prefix_hash = md5(secret_key.strip().encode())

    for number in range(1, 1 << 32):
        candidate_hash = prefix_hash.copy()
        candidate_hash.update(str(number).encode())
        if candidate_hash.digest()[:3] == b"\x00\x00\x00":
            return number

    raise RuntimeError("no qualifying suffix found before the search limit")
