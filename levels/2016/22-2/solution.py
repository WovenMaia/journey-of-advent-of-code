"""Solution for Advent of Code 2016, Day 22, Part 2."""

from collections import deque
from pathlib import Path
import re

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "22.txt"
NODE_RE = re.compile(r"^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T")


def parse_nodes(text: str) -> dict[tuple[int, int], tuple[int, int, int]]:
    nodes = {}
    for line in text.splitlines():
        match = NODE_RE.match(line.strip())
        if match:
            x, y, size, used, available = map(int, match.groups())
            nodes[(x, y)] = (size, used, available)
    if not nodes:
        raise ValueError("input has no grid nodes")
    return nodes


def shortest_steps(text: str) -> int:
    nodes = parse_nodes(text)
    empties = [position for position, (_, used, _) in nodes.items() if used == 0]
    if len(empties) != 1:
        raise ValueError("input must contain exactly one empty node")
    empty = empties[0]
    empty_capacity = nodes[empty][0]
    open_cells = {
        position for position, (_, used, _) in nodes.items() if used <= empty_capacity
    }
    goal = max((position for position in nodes if position[1] == 0), key=lambda p: p[0])
    origin = (0, 0)
    if origin not in nodes:
        raise ValueError("grid has no origin node")
    queue = deque([(empty, goal, 0)])
    visited = {(empty, goal)}
    while queue:
        empty, goal, distance = queue.popleft()
        if goal == origin:
            return distance
        x, y = empty
        for neighbor in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if neighbor not in open_cells or neighbor == goal:
                continue
            state = (neighbor, goal)
            if state not in visited:
                visited.add(state)
                queue.append((neighbor, goal, distance + 1))
        if goal in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            state = (goal, empty)
            if state not in visited:
                visited.add(state)
                queue.append((goal, empty, distance + 1))
    raise ValueError("goal data cannot reach the origin")


def run(text: str) -> dict[str, int]:
    return {"a": shortest_steps(text)}


def main() -> int:
    print(shortest_steps(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
