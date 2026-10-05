"""Solution for Advent of Code 2016, Day 14, Part 2."""

from hashlib import md5
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "14.txt"


def hash_at(salt: str, index: int) -> str:
    """Return the 2017-round stretched hash for one salt/index pair."""
    digest = md5(f"{salt}{index}".encode(), usedforsecurity=False).hexdigest()
    for _ in range(2016):
        digest = md5(digest.encode(), usedforsecurity=False).hexdigest()
    return digest


def first_triplet(digest: str) -> str | None:
    """Return the first character in a run of three, if present."""
    for left, middle, right in zip(digest, digest[1:], digest[2:]):
        if left == middle == right:
            return left
    return None


def key_index(salt: str, key_count: int = 64) -> int:
    """Find the requested key index with cached stretched hashes."""
    cache: list[str] = []

    def get(index: int) -> str:
        while len(cache) <= index:
            cache.append(hash_at(salt, len(cache)))
        return cache[index]

    found = 0
    index = 0
    while found < key_count:
        digest = get(index)
        character = first_triplet(digest)
        if character and any(character * 5 in get(next_index) for next_index in range(index + 1, index + 1001)):
            found += 1
            if found == key_count:
                return index
        index += 1
    raise RuntimeError("key search did not terminate")


def run(text: str) -> dict[str, int]:
    """Solve the puzzle for the supplied salt."""
    return {"a": key_index(text.strip())}


def main() -> int:
    print(run(INPUT_PATH.read_text(encoding="utf-8"))["a"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
