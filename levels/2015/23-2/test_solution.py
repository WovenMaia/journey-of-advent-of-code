"""Public examples for Advent of Code 2015, Day 23, Part 2."""

import unittest

from solution import parse_program, run


class ProgramExamples(unittest.TestCase):
    def test_initial_a_is_supported(self) -> None:
        program = parse_program("inc a\njio a, +2\ntpl a\ninc a\n")
        self.assertEqual(run(program), (7, 0))

    def test_initial_a_can_be_overridden_for_shared_machine(self) -> None:
        program = parse_program("inc b\n")
        self.assertEqual(run(program, initial_a=0), (0, 1))


if __name__ == "__main__":
    unittest.main()
