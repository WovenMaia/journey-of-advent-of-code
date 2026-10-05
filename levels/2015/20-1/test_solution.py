"""Public examples for Advent of Code 2015, Day 20, Part 1."""

import unittest

from solution import part_one, target_presents


class HouseExamples(unittest.TestCase):
    def test_first_houses_match_public_totals(self) -> None:
        self.assertEqual(part_one("10"), 1)
        self.assertEqual(part_one("70"), 4)

    def test_parser_rejects_invalid_target(self) -> None:
        with self.assertRaises(ValueError):
            target_presents("0")


if __name__ == "__main__":
    unittest.main()
