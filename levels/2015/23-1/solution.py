"""Solution for Advent of Code 2015, Day 23, Part 1."""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Instruction:
    operation: str
    register: str | None = None
    offset: int | None = None


def parse_program(document: str) -> tuple[Instruction, ...]:
    program: list[Instruction] = []
    for line in document.splitlines():
        if not line:
            continue
        parts = line.replace(",", "").split()
        if parts[0] in {"hlf", "tpl", "inc"} and len(parts) == 2:
            program.append(Instruction(parts[0], parts[1]))
        elif parts[0] == "jmp" and len(parts) == 2:
            program.append(Instruction(parts[0], offset=int(parts[1])))
        elif parts[0] in {"jie", "jio"} and len(parts) == 3:
            program.append(Instruction(parts[0], parts[1], int(parts[2])))
        else:
            raise ValueError(f"invalid instruction: {line!r}")
    return tuple(program)


def run(program: tuple[Instruction, ...], initial_a: int = 0) -> tuple[int, int]:
    registers = {"a": initial_a, "b": 0}
    pointer = 0
    while 0 <= pointer < len(program):
        instruction = program[pointer]
        operation = instruction.operation
        if operation == "hlf":
            registers[instruction.register] //= 2
            pointer += 1
        elif operation == "tpl":
            registers[instruction.register] *= 3
            pointer += 1
        elif operation == "inc":
            registers[instruction.register] += 1
            pointer += 1
        elif operation == "jmp":
            pointer += instruction.offset
        elif operation == "jie":
            pointer += instruction.offset if registers[instruction.register] % 2 == 0 else 1
        else:
            pointer += instruction.offset if registers[instruction.register] == 1 else 1
    return registers["a"], registers["b"]


def part_one(document: str) -> int:
    return run(parse_program(document))[1]


if __name__ == "__main__":
    with open("inputs/2015/23.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
