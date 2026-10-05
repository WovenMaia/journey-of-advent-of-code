"""Solution for Advent of Code 2015, Day 22, Part 2."""

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
    return State(state.player_hp, state.mana + (101 if state.recharge else 0), state.boss_hp - (3 if state.poison else 0), state.boss_damage, max(0, state.shield - 1), max(0, state.poison - 1), max(0, state.recharge - 1), state.spent)


def minimum_mana(document: str, player_hp: int = 50, mana: int = 500) -> int:
    boss_hp, boss_damage = parse_boss(document)
    start = State(player_hp, mana, boss_hp, boss_damage, 0, 0, 0, 0)
    queue: list[tuple[int, int, State]] = [(0, 0, start)]
    seen: dict[tuple[int, int, int, int, int, int], int] = {}
    best = float("inf")
    serial = 1
    while queue:
        _, _, state = heapq.heappop(queue)
        if state.spent >= best:
            continue
        key = (state.player_hp, state.mana, state.boss_hp, state.shield, state.poison, state.recharge)
        if state.spent >= seen.get(key, 10**9):
            continue
        seen[key] = state.spent
        if state.player_hp <= 1:
            continue
        state = State(state.player_hp - 1, state.mana, state.boss_hp, state.boss_damage, state.shield, state.poison, state.recharge, state.spent)
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
            cast = effects(cast)
            if cast.boss_hp <= 0:
                best = min(best, cast.spent)
                continue
            damage = max(1, cast.boss_damage - (7 if cast.shield else 0))
            if cast.player_hp <= damage:
                continue
            next_state = State(cast.player_hp - damage, cast.mana, cast.boss_hp, cast.boss_damage, cast.shield, cast.poison, cast.recharge, cast.spent)
            heapq.heappush(queue, (next_state.spent, serial, next_state))
            serial += 1
    if best == float("inf"):
        raise ValueError("no winning spell sequence")
    return int(best)


def part_two(document: str) -> int:
    return minimum_mana(document)


if __name__ == "__main__":
    with open("inputs/2015/22.txt", encoding="utf-8") as input_file:
        print(part_two(input_file.read()))
