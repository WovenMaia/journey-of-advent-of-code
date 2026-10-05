"""Solution for Advent of Code 2016, Day 12, Part 2."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "12.txt"
REGISTERS = frozenset("abcd")


def run(text: str, initial_c: int = 1) -> dict[str, int]:
    """Execute assembunny with part two's initial c value."""
    program = [line.split() for line in text.splitlines() if line.strip()]
    registers = {name: 0 for name in REGISTERS}
    registers["c"] = initial_c
    pointer = 0

    def value(token: str) -> int:
        return registers[token] if token in REGISTERS else int(token)

    while 0 <= pointer < len(program):
        instruction = program[pointer]
        operation = instruction[0]
        if operation == "cpy" and len(instruction) == 3:
            if instruction[2] in REGISTERS:
                registers[instruction[2]] = value(instruction[1])
            pointer += 1
        elif operation == "inc" and len(instruction) == 2:
            if instruction[1] in REGISTERS:
                registers[instruction[1]] += 1
            pointer += 1
        elif operation == "dec" and len(instruction) == 2:
            if instruction[1] in REGISTERS:
                registers[instruction[1]] -= 1
            pointer += 1
        elif operation == "jnz" and len(instruction) == 3:
            pointer += value(instruction[2]) if value(instruction[1]) != 0 else 1
        else:
            raise ValueError(f"invalid instruction: {' '.join(instruction)!r}")
    return registers


def main() -> int:
    print(run(INPUT_PATH.read_text(encoding="utf-8"))["a"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
