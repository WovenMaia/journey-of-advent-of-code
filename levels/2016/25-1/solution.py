"""Solution for Advent of Code 2016, Day 25, Part 1."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "25.txt"
REGISTERS = "abcd"


def _value(token: str, registers: dict[str, int]) -> int:
    if token in registers:
        return registers[token]
    return int(token)


def signal(text: str, initial_a: int, output_count: int = 20, max_steps: int = 1_000_000) -> list[int]:
    program = [line.split() for line in text.splitlines() if line.strip()]
    registers = {name: 0 for name in REGISTERS}
    registers["a"] = initial_a
    pointer = 0
    outputs = []
    for _ in range(max_steps):
        if not 0 <= pointer < len(program):
            return outputs
        operation, *args = program[pointer]
        if operation == "cpy" and len(args) == 2 and args[1] in registers:
            registers[args[1]] = _value(args[0], registers)
        elif operation == "inc" and len(args) == 1 and args[0] in registers:
            registers[args[0]] += 1
        elif operation == "dec" and len(args) == 1 and args[0] in registers:
            registers[args[0]] -= 1
        elif operation == "jnz" and len(args) == 2:
            if _value(args[0], registers) != 0:
                pointer += _value(args[1], registers)
                continue
        elif operation == "out" and len(args) == 1:
            value = _value(args[0], registers)
            if value not in (0, 1) or (outputs and value == outputs[-1]):
                return outputs
            outputs.append(value)
            if len(outputs) == output_count:
                return outputs
        pointer += 1
    return outputs


def lowest_clock_seed(text: str, output_count: int = 20) -> int:
    for candidate in range(1, 1_000_000):
        if len(signal(text, candidate, output_count)) == output_count:
            return candidate
    raise ValueError("no clock seed found below search limit")


def run(text: str) -> dict[str, int]:
    return {"a": lowest_clock_seed(text)}


def main() -> int:
    print(lowest_clock_seed(INPUT_PATH.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
