"""Solution for Advent of Code 2016, Day 10, Part 2."""

import re
from collections import defaultdict, deque
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "10.txt"
VALUE = re.compile(r"value (\d+) goes to bot (\d+)")
RULE = re.compile(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)")


def output_product(text: str) -> int:
    """Return the product of the chips in output bins 0, 1, and 2."""
    bots: dict[int, list[int]] = defaultdict(list)
    outputs: dict[int, int] = {}
    rules: dict[int, tuple[tuple[str, int], tuple[str, int]]] = {}
    queue: deque[int] = deque()
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if match := VALUE.fullmatch(line):
            value, bot = map(int, match.groups())
            bots[bot].append(value)
            if len(bots[bot]) == 2:
                queue.append(bot)
        elif match := RULE.fullmatch(line):
            bot, low_kind, low_id, high_kind, high_id = match.groups()
            rules[int(bot)] = ((low_kind, int(low_id)), (high_kind, int(high_id)))
        else:
            raise ValueError(f"invalid instruction: {line!r}")
    while queue:
        bot = queue.popleft()
        chips = bots[bot]
        if len(chips) < 2:
            continue
        rule = rules.get(bot)
        if rule is None:
            raise ValueError(f"missing rule for bot {bot}")
        bots[bot] = []
        for value, (kind, recipient) in zip(sorted(chips), rule):
            if kind == "output":
                outputs[recipient] = value
            else:
                bots[recipient].append(value)
                if len(bots[recipient]) == 2:
                    queue.append(recipient)
    try:
        return outputs[0] * outputs[1] * outputs[2]
    except KeyError as error:
        raise ValueError("outputs 0, 1, and 2 are not all filled") from error


def main() -> int:
    print(output_product(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
