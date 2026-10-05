"""Completion check for Advent of Code 2016, Day 25, Part 2."""

import unittest

from solution import part_two


class FinalStarExamples(unittest.TestCase):
    def test_final_star_is_granted(self) -> None:
        self.assertEqual(part_two(), "granted")

    def test_input_text_does_not_change_the_grant(self) -> None:
        self.assertEqual(part_two("out 0\n"), "granted")


if __name__ == "__main__":
    unittest.main()
