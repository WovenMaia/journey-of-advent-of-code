"""Published examples for Advent of Code 2016, Day 23, Part 2."""

import unittest

from solution import execute


class ToggleExamples(unittest.TestCase):
    def test_published_program_still_interprets_toggles(self) -> None:
        program = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
"""
        self.assertEqual(execute(program, initial_a=2)["a"], 3)

    def test_nested_addition_loop_is_collapsed(self) -> None:
        program = """cpy 3 b
cpy 2 d
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
"""
        self.assertEqual(execute(program, initial_a=0)["a"], 6)

    def test_part_two_initial_register_is_twelve(self) -> None:
        self.assertEqual(execute("inc a\n")["a"], 13)


if __name__ == "__main__":
    unittest.main()
