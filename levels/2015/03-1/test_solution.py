"""Public examples for Advent of Code 2015, Day 3, Part 1."""

import unittest

from solution import houses_visited


class HousesVisitedExamples(unittest.TestCase):
    def test_single_move_visits_two_houses(self) -> None:
        self.assertEqual(houses_visited(">"), 2)

    def test_square_visits_four_houses(self) -> None:
        self.assertEqual(houses_visited("^>v<"), 4)

    def test_repeated_vertical_moves_revisit_two_houses(self) -> None:
        self.assertEqual(houses_visited("^v^v^v^v^v"), 2)

    def test_starting_house_counts_without_moves(self) -> None:
        self.assertEqual(houses_visited(""), 1)

    def test_rejects_unknown_direction(self) -> None:
        with self.assertRaisesRegex(ValueError, "position 2"):
            houses_visited("^x")


if __name__ == "__main__":
    unittest.main()
