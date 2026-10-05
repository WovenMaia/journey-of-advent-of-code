"""Published examples for Advent of Code 2016, Day 23, Part 1."""

import unittest

from solution import execute


class ToggleExamples(unittest.TestCase):
    def test_published_program_leaves_three_in_a(self) -> None:
        program = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
"""
        self.assertEqual(execute(program)["a"], 3)

    def test_toggled_instruction_with_invalid_register_is_skipped(self) -> None:
        self.assertEqual(execute("cpy 1 a\ntgl a\ninc 1\ninc a\n")["a"], 2)

    def test_initial_register_is_configurable(self) -> None:
        self.assertEqual(execute("inc a\n", initial_a=4)["a"], 5)


if __name__ == "__main__":
    unittest.main()
