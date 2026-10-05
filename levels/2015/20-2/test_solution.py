"""Public examples for Advent of Code 2015, Day 20, Part 2."""

import unittest

from solution import part_two


class LimitedElfExamples(unittest.TestCase):
    def test_house_eight_reaches_150_with_limited_visits(self) -> None:
        self.assertEqual(part_two("150"), 8)

    def test_house_one_gets_eleven(self) -> None:
        self.assertEqual(part_two("11"), 1)


if __name__ == "__main__":
    unittest.main()
