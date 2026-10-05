"""Solution for Advent of Code 2015, Day 7, Part 2."""

from collections.abc import Iterable
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


_PART1_PATH = Path(__file__).resolve().parents[1] / "07-1" / "solution.py"
_PART1_SPEC = spec_from_file_location("day07_part1", _PART1_PATH)
if _PART1_SPEC is None or _PART1_SPEC.loader is None:
    raise ImportError(f"cannot load Part 1 evaluator from {_PART1_PATH}")
_PART1 = module_from_spec(_PART1_SPEC)
_PART1_SPEC.loader.exec_module(_PART1)
evaluate_circuit = _PART1.evaluate_circuit


def evaluate_rewired_circuit(
    instructions: Iterable[str], override_wire: str = "b", target: str = "a"
) -> int:
    """Evaluate *target* after replacing *override_wire* with Part 1's target."""
    original = tuple(instructions)
    signal = evaluate_circuit(original, "a")

    rewired: list[str] = []
    replaced = False
    for raw_instruction in original:
        parts = raw_instruction.strip().split(" -> ")
        if len(parts) == 2 and parts[1] == override_wire:
            rewired.append(f"{signal} -> {override_wire}")
            replaced = True
        else:
            rewired.append(raw_instruction)

    if not replaced:
        rewired.append(f"{signal} -> {override_wire}")
    return evaluate_circuit(rewired, target)
