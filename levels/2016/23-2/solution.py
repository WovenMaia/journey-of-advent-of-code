"""Solution for Advent of Code 2016, Day 23, Part 2."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "23.txt"
REGISTERS = "abcd"


def _value(token: str, registers: dict[str, int]) -> int:
    if token in registers:
        return registers[token]
    return int(token)


def _multiply(program: list[list[str]], pointer: int, registers: dict[str, int]) -> bool:
    """Collapse the six instruction nested addition loop used by the input."""
    if pointer + 5 >= len(program):
        return False
    first, second, third, fourth, fifth, sixth = program[pointer : pointer + 6]
    if (
        first[0] == "cpy"
        and len(first) == 3
        and first[2] in registers
        and second == ["inc", second[1]]
        and len(second) == 2
        and second[1] in registers
        and third == ["dec", first[2]]
        and fourth == ["jnz", first[2], "-2"]
        and fifth[0] == "dec"
        and len(fifth) == 2
        and fifth[1] in registers
        and sixth == ["jnz", fifth[1], "-5"]
        and first[1] in registers
        and second[1] != first[2]
        and fifth[1] != first[2]
    ):
        registers[second[1]] += registers[first[1]] * registers[fifth[1]]
        registers[first[2]] = 0
        registers[fifth[1]] = 0
        return True
    return False


def execute(text: str, initial_a: int = 12) -> dict[str, int]:
    program = [line.split() for line in text.splitlines() if line.strip()]
    registers = {name: 0 for name in REGISTERS}
    registers["a"] = initial_a
    pointer = 0
    steps = 0
    while 0 <= pointer < len(program):
        steps += 1
        if steps > 50_000_000:
            raise ValueError("program exceeded the execution limit")
        if _multiply(program, pointer, registers):
            pointer += 6
            continue
        instruction = program[pointer]
        operation, args = instruction[0], instruction[1:]
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
        elif operation == "tgl" and len(args) == 1:
            target = pointer + _value(args[0], registers)
            if 0 <= target < len(program):
                if len(program[target]) == 2:
                    program[target][0] = "dec" if program[target][0] == "inc" else "inc"
                elif len(program[target]) == 3:
                    program[target][0] = "cpy" if program[target][0] == "jnz" else "jnz"
        pointer += 1
    return registers


def run(text: str) -> dict[str, int]:
    return {"a": execute(text)["a"]}


def main() -> int:
    print(execute(INPUT_PATH.read_text(encoding="utf-8"))["a"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
