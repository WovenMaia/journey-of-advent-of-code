"""Published examples for Advent of Code 2016, Day 21, Part 1."""

import unittest

from solution import scramble


EXAMPLE = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
"""


class ScrambleExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(scramble(EXAMPLE, "abcde"), "decab")

    def test_each_operation_and_rotation_wrap(self) -> None:
        self.assertEqual(scramble("swap letter a with letter d", "abcd"), "dbca")
        self.assertEqual(scramble("rotate right 5 steps", "abcd"), "dabc")
        self.assertEqual(scramble("move position 0 to position 3", "abcd"), "bcda")

    def test_unknown_instruction_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "unrecognized"):
            scramble("teleport 1", "abc")


if __name__ == "__main__":
    unittest.main()
