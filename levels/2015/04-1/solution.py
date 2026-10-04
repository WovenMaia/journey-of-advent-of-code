"""Solution for Advent of Code 2015, Day 4, Part 1."""

from hashlib import md5


def lowest_adventcoin_number(secret_key: str) -> int:
    """Return the lowest positive suffix whose MD5 hash begins with five zeroes."""
    prefix_hash = md5(secret_key.strip().encode())

    for number in range(1, 1 << 32):
        candidate_hash = prefix_hash.copy()
        candidate_hash.update(str(number).encode())
        digest = candidate_hash.digest()
        if digest[0] == 0 and digest[1] == 0 and digest[2] < 16:
            return number

    raise RuntimeError("no qualifying suffix found before the search limit")
