"""Published examples for Advent of Code 2016, Day 21, Part 2."""

import unittest

from solution import unscramble


EXAMPLE = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
"""


class UnscrambleExamples(unittest.TestCase):
    def test_published_example_reverses_the_scramble(self) -> None:
        self.assertEqual(unscramble(EXAMPLE, "decab"), "abcde")

    def test_inverse_move_and_rotate_based(self) -> None:
        self.assertEqual(
            unscramble("move position 0 to position 3", "bcda"), "abcd"
        )
        self.assertEqual(
            unscramble("rotate based on position of letter a", "dabc"), "abcd"
        )

    def test_unknown_instruction_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "unrecognized"):
            unscramble("teleport 1", "abc")


if __name__ == "__main__":
    unittest.main()
