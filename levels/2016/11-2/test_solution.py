"""Public examples for Advent of Code 2016, Day 11, Part 2."""

import unittest

from solution import minimum_steps


class ElevatorExamples(unittest.TestCase):

    def test_three_pairs_starting_together(self) -> None:
        text = "The first floor contains a hydrogen generator and a hydrogen-compatible microchip."
        self.assertEqual(minimum_steps(text), 27)
    def test_unreachable_configuration_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "incomplete component pair"):
            minimum_steps("The first floor contains a hydrogen generator.")


if __name__ == "__main__":
    unittest.main()
