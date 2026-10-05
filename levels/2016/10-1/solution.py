"""Solution for Advent of Code 2016, Day 10, Part 1."""

import re
from collections import defaultdict, deque
from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "10.txt"
VALUE = re.compile(r"value (\d+) goes to bot (\d+)")
RULE = re.compile(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)")


def comparing_bot(text: str, target: tuple[int, int] = (17, 61)) -> int:
    """Return the bot that compares the two target chip values."""
    bots: dict[int, list[int]] = defaultdict(list)
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
    low, high = sorted(target)
    while queue:
        bot = queue.popleft()
        chips = bots[bot]
        if len(chips) < 2:
            continue
        if low in chips and high in chips:
            return bot
        rule = rules.get(bot)
        if rule is None:
            raise ValueError(f"missing rule for bot {bot}")
        values = sorted(chips)
        bots[bot] = []
        for value, (kind, recipient) in zip(values, rule):
            if kind == "bot":
                bots[recipient].append(value)
                if len(bots[recipient]) == 2:
                    queue.append(recipient)
    raise ValueError("target comparison never occurred")


def main() -> int:
    print(comparing_bot(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
