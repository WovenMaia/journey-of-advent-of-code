"""Solution for Advent of Code 2015, Day 22, Part 1."""

from dataclasses import dataclass
import heapq
import re


@dataclass(frozen=True)
class State:
    player_hp: int
    mana: int
    boss_hp: int
    boss_damage: int
    shield: int
    poison: int
    recharge: int
    spent: int


SPELLS = ((53, "missile"), (73, "drain"), (113, "shield"), (173, "poison"), (229, "recharge"))


def parse_boss(document: str) -> tuple[int, int]:
    values = [int(value) for value in re.findall(r"-?\d+", document)]
    if len(values) != 2 or any(value <= 0 for value in values):
        raise ValueError("expected positive boss hit points and damage")
    return tuple(values)  # type: ignore[return-value]


def effects(state: State) -> State:
    boss_hp = state.boss_hp - (3 if state.poison else 0)
    return State(
        state.player_hp,
        state.mana + (101 if state.recharge else 0),
        boss_hp,
        state.boss_damage,
        max(0, state.shield - 1),
        max(0, state.poison - 1),
        max(0, state.recharge - 1),
        state.spent,
    )


def minimum_mana(document: str, player_hp: int = 50, mana: int = 500) -> int:
    boss_hp, boss_damage = parse_boss(document)
    queue: list[tuple[int, int, State]] = []
    start = State(player_hp, mana, boss_hp, boss_damage, 0, 0, 0, 0)
    heapq.heappush(queue, (0, 0, start))
    seen: dict[tuple[int, int, int, int, int, int, int], int] = {}
    best = float("inf")
    sequence = 1
    while queue:
        _, _, state = heapq.heappop(queue)
        if state.spent >= best:
            continue
        key = (state.player_hp, state.mana, state.boss_hp, state.shield, state.poison, state.recharge, state.boss_damage)
        if state.spent >= seen.get(key, 10**9):
            continue
        seen[key] = state.spent
        state = effects(state)
        if state.boss_hp <= 0:
            best = min(best, state.spent)
            continue
        for cost, spell in SPELLS:
            if cost > state.mana or (spell == "shield" and state.shield) or (spell == "poison" and state.poison) or (spell == "recharge" and state.recharge):
                continue
            cast = State(state.player_hp, state.mana - cost, state.boss_hp, state.boss_damage, state.shield, state.poison, state.recharge, state.spent + cost)
            if spell == "missile":
                cast = State(cast.player_hp, cast.mana, cast.boss_hp - 4, cast.boss_damage, cast.shield, cast.poison, cast.recharge, cast.spent)
            elif spell == "drain":
                cast = State(cast.player_hp + 2, cast.mana, cast.boss_hp - 2, cast.boss_damage, cast.shield, cast.poison, cast.recharge, cast.spent)
            elif spell == "shield":
                cast = State(cast.player_hp, cast.mana, cast.boss_hp, cast.boss_damage, 6, cast.poison, cast.recharge, cast.spent)
            elif spell == "poison":
                cast = State(cast.player_hp, cast.mana, cast.boss_hp, cast.boss_damage, cast.shield, 6, cast.recharge, cast.spent)
            else:
                cast = State(cast.player_hp, cast.mana, cast.boss_hp, cast.boss_damage, cast.shield, cast.poison, 5, cast.spent)
            if cast.boss_hp <= 0:
                best = min(best, cast.spent)
                continue
            after_boss_effects = effects(cast)
            if after_boss_effects.boss_hp <= 0:
                best = min(best, after_boss_effects.spent)
                continue
            damage = max(1, after_boss_effects.boss_damage - (7 if after_boss_effects.shield else 0))
            if after_boss_effects.player_hp <= damage:
                continue
            next_state = State(after_boss_effects.player_hp - damage, after_boss_effects.mana, after_boss_effects.boss_hp, after_boss_effects.boss_damage, after_boss_effects.shield, after_boss_effects.poison, after_boss_effects.recharge, after_boss_effects.spent)
            heapq.heappush(queue, (next_state.spent, sequence, next_state))
            sequence += 1
    if best == float("inf"):
        raise ValueError("no winning spell sequence")
    return int(best)


def part_one(document: str) -> int:
    return minimum_mana(document)


if __name__ == "__main__":
    with open("inputs/2015/22.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
