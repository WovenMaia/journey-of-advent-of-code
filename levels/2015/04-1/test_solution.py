"""Public examples for Advent of Code 2015, Day 4, Part 1."""

import unittest

from solution import lowest_adventcoin_number


class AdventCoinExamples(unittest.TestCase):
    def test_abcdef_requires_609043(self) -> None:
        self.assertEqual(lowest_adventcoin_number("abcdef"), 609043)

    def test_pqrstuv_requires_1048970(self) -> None:
        self.assertEqual(lowest_adventcoin_number("pqrstuv"), 1048970)


if __name__ == "__main__":
    unittest.main()
