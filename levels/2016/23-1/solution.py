"""Solution for Advent of Code 2016, Day 23, Part 1."""

from pathlib import Path

INPUT_PATH = Path(__file__).resolve().parents[3] / "inputs" / "2016" / "23.txt"
REGISTERS = "abcd"


def _value(token: str, registers: dict[str, int]) -> int:
    if token in registers:
        return registers[token]
    return int(token)

def execute(text: str, initial_a: int = 7) -> dict[str, int]:
    """Run assembunny with self modifying `tgl` instructions."""
    program = [line.split() for line in text.splitlines() if line.strip()]
    registers = {name: 0 for name in REGISTERS}
    registers["a"] = initial_a
    pointer = 0
    steps = 0
    while 0 <= pointer < len(program):
        steps += 1
        if steps > 50_000_000:
            raise ValueError("program exceeded the execution limit")
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
                target_args = program[target][1:]
                if len(target_args) == 1:
                    program[target][0] = "dec" if program[target][0] == "inc" else "inc"
                elif len(target_args) == 2:
                    program[target][0] = "cpy" if program[target][0] == "jnz" else "jnz"
        pointer += 1
    return registers


def run(text: str) -> dict[str, int]:
    return {"a": execute(text, 7)["a"]}


def main() -> int:
    print(execute(INPUT_PATH.read_text(encoding="utf-8"))["a"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
