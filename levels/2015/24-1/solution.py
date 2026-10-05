"""Solution for Advent of Code 2015, Day 24, Part 1."""

from functools import cache
from itertools import combinations
from math import prod


def parse_weights(document: str) -> tuple[int, ...]:
    weights = tuple(sorted(int(line) for line in document.splitlines() if line))
    if not weights or any(weight <= 0 for weight in weights):
        raise ValueError("weights must be positive")
    return weights


def _subset_masks(weights: tuple[int, ...], mask: int, target: int, required: int = -1, max_size: int | None = None):
    indices = [index for index in range(len(weights)) if mask & (1 << index)]

    def visit(start: int, remaining: int, selected: int) -> object:
        if remaining == 0:
            if required < 0 or selected & (1 << required):
                yield selected
            return
        if max_size is not None and selected.bit_count() >= max_size:
            return
        for position in range(start, len(indices)):
            index = indices[position]
            weight = weights[index]
            if weight > remaining:
                break
            yield from visit(position + 1, remaining - weight, selected | (1 << index))

    yield from visit(0, target, 0)


def _can_split(weights: tuple[int, ...], mask: int, groups: int, target: int) -> bool:
    @cache
    def search(current: int, count: int) -> bool:
        if count == 1:
            return sum(weights[index] for index in range(len(weights)) if current & (1 << index)) == target
        required = (current & -current).bit_length() - 1
        return any(search(current ^ subset, count - 1) for subset in _subset_masks(weights, current, target, required))

    return search(mask, groups)


def _best(weights: tuple[int, ...], groups: int) -> int:
    total = sum(weights)
    if total % groups:
        raise ValueError("weights cannot be split evenly")
    target = total // groups
    full_mask = (1 << len(weights)) - 1
    for size in range(1, len(weights) + 1):
        candidates = []
        for subset in _subset_masks(weights, full_mask, target, max_size=size):
            if subset.bit_count() != size:
                continue
            selected = [weights[index] for index in range(len(weights)) if subset & (1 << index)]
            candidates.append((prod(selected), subset))
        for quantum_entanglement, subset in sorted(candidates):
            if _can_split(weights, full_mask ^ subset, groups - 1, target):
                return quantum_entanglement
    raise ValueError("no valid partition")


def part_one(document: str) -> int:
    return _best(parse_weights(document), 3)


if __name__ == "__main__":
    with open("inputs/2015/24.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
