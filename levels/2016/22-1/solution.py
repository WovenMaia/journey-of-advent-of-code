"""Solution for Advent of Code 2016, Day 22, Part 1."""

from pathlib import Path
import re

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "22.txt"
NODE_RE = re.compile(r"^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T")


def parse_nodes(text: str) -> list[tuple[int, int, int, int, int]]:
    nodes = []
    for line in text.splitlines():
        match = NODE_RE.match(line.strip())
        if match:
            nodes.append(tuple(map(int, match.groups())))
    if not nodes:
        raise ValueError("input has no grid nodes")
    return nodes


def viable_pairs(text: str) -> int:
    nodes = parse_nodes(text)
    return sum(
        used_a > 0 and index_a != index_b and used_a <= avail_b
        for index_a, (_, _, _, used_a, _) in enumerate(nodes)
        for index_b, (_, _, _, _, avail_b) in enumerate(nodes)
    )


def run(text: str) -> dict[str, int]:
    return {"a": viable_pairs(text)}


def main() -> int:
    print(viable_pairs(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
