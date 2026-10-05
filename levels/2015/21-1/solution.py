"""Solution for Advent of Code 2015, Day 21, Part 1."""

from itertools import combinations
import re

WEAPONS = ((8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0))
ARMOR = ((0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5))
RINGS = ((25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3))


def parse_boss(document: str) -> tuple[int, int, int]:
    values = [int(value) for value in re.findall(r"-?\d+", document)]
    if len(values) != 3 or any(value < 0 for value in values):
        raise ValueError("expected boss hit points, damage, and armor")
    return tuple(values)  # type: ignore[return-value]


def loadouts() -> tuple[tuple[int, int, int, int], ...]:
    choices: list[tuple[int, int, int, int]] = []
    for weapon in WEAPONS:
        for armor in ARMOR:
            for count in range(3):
                for rings in combinations(RINGS, count):
                    items = (weapon, armor, *rings)
                    choices.append(tuple(sum(item[index] for item in items) for index in range(3)) + (0,))
    return tuple(choices)


def wins(player_damage: int, player_armor: int, boss: tuple[int, int, int]) -> bool:
    player_hp = 100
    boss_hp, boss_damage, boss_armor = boss
    player_hit = max(1, player_damage - boss_armor)
    boss_hit = max(1, boss_damage - player_armor)
    return (boss_hp + player_hit - 1) // player_hit <= (player_hp + boss_hit - 1) // boss_hit


def part_one(document: str) -> int:
    boss = parse_boss(document)
    costs = [loadout[0] for loadout in loadouts() if wins(loadout[1], loadout[2], boss)]
    return min(costs)


if __name__ == "__main__":
    with open("inputs/2015/21.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
