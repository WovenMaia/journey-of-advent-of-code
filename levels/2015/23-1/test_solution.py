"""Public examples for Advent of Code 2015, Day 23, Part 1."""

import unittest

from solution import parse_program, run


class ProgramExamples(unittest.TestCase):
    def test_public_program_sets_a_to_two(self) -> None:
        program = parse_program("inc a\njio a, +2\ntpl a\ninc a\n")
        self.assertEqual(run(program), (2, 0))

    def test_jie_checks_even_register(self) -> None:
        program = parse_program("inc a\njie a, +2\ninc b\ninc b\n")
        self.assertEqual(run(program), (1, 2))


if __name__ == "__main__":
    unittest.main()
