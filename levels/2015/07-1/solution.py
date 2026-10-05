"""Solution for Advent of Code 2015, Day 7, Part 1."""

from collections.abc import Iterable
import re


MASK = 0xFFFF
_WIRE = re.compile(r"^[a-z]+$")
_OPERATIONS = {"AND", "OR", "LSHIFT", "RSHIFT"}


def evaluate_circuit(instructions: Iterable[str], target: str = "a") -> int:
    """Evaluate *target* from the circuit instructions using 16-bit signals."""
    wires: dict[str, tuple[str, ...]] = {}

    for raw_instruction in instructions:
        instruction = raw_instruction.strip()
        parts = instruction.split(" -> ")
        if len(parts) != 2:
            raise ValueError(f"invalid instruction: {raw_instruction!r}")

        expression, destination = parts
        if _WIRE.fullmatch(destination) is None or destination in wires:
            raise ValueError(f"invalid destination: {raw_instruction!r}")

        tokens = tuple(expression.split())
        if len(tokens) == 1:
            if not _is_operand(tokens[0]):
                raise ValueError(f"invalid expression: {raw_instruction!r}")
        elif len(tokens) == 2:
            if tokens[0] != "NOT" or not _is_operand(tokens[1]):
                raise ValueError(f"invalid expression: {raw_instruction!r}")
        elif len(tokens) == 3:
            if tokens[1] not in _OPERATIONS or not all(
                _is_operand(token) for token in (tokens[0], tokens[2])
            ):
                raise ValueError(f"invalid expression: {raw_instruction!r}")
        else:
            raise ValueError(f"invalid expression: {raw_instruction!r}")
        wires[destination] = tokens

    memo: dict[str, int] = {}
    visiting: set[str] = set()

    def resolve(token: str) -> int:
        if token.isdigit():
            return int(token) & MASK
        if token not in wires:
            raise ValueError(f"undefined wire: {token!r}")
        if token in memo:
            return memo[token]
        if token in visiting:
            raise ValueError(f"cyclic circuit at wire: {token!r}")

        visiting.add(token)
        operation = wires[token]
        if len(operation) == 1:
            value = resolve(operation[0])
        elif len(operation) == 2:
            value = ~resolve(operation[1])
        else:
            left = resolve(operation[0])
            right = resolve(operation[2])
            if operation[1] == "AND":
                value = left & right
            elif operation[1] == "OR":
                value = left | right
            elif operation[1] == "LSHIFT":
                value = left << right
            else:
                value = left >> right

        visiting.remove(token)
        memo[token] = value & MASK
        return memo[token]

    return resolve(target)


def _is_operand(token: str) -> bool:
    return token.isdigit() or _WIRE.fullmatch(token) is not None
