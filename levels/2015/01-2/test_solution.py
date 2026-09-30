"""Public examples for Advent of Code 2015, Day 1, Part 2."""

import unittest

from solution import first_basement_position


class FirstBasementPositionExamples(unittest.TestCase):
    def test_first_instruction_can_enter_basement(self) -> None:
        self.assertEqual(first_basement_position(")"), 1)

    def test_later_instruction_can_enter_basement(self) -> None:
        self.assertEqual(first_basement_position("()())"), 5)

    def test_returns_none_when_basement_is_never_reached(self) -> None:
        self.assertIsNone(first_basement_position("(()())"))

    def test_rejects_non_instruction_characters(self) -> None:
        with self.assertRaisesRegex(ValueError, "position 2"):
            first_basement_position("(x)")


if __name__ == "__main__":
    unittest.main()
