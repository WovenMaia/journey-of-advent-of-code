"""Public examples for Advent of Code 2015, Day 3, Part 2."""

import unittest

from solution import houses_visited_with_robot


class RobotDeliveryExamples(unittest.TestCase):
    def test_two_opposite_moves_visit_three_houses(self) -> None:
        self.assertEqual(houses_visited_with_robot("^v"), 3)

    def test_square_directions_visit_three_houses(self) -> None:
        self.assertEqual(houses_visited_with_robot("^>v<"), 3)

    def test_alternating_vertical_moves_visit_eleven_houses(self) -> None:
        self.assertEqual(houses_visited_with_robot("^v^v^v^v^v"), 11)

    def test_starting_house_counts_without_moves(self) -> None:
        self.assertEqual(houses_visited_with_robot(""), 1)

    def test_rejects_unknown_direction(self) -> None:
        with self.assertRaisesRegex(ValueError, "position 2"):
            houses_visited_with_robot("^x")


if __name__ == "__main__":
    unittest.main()
