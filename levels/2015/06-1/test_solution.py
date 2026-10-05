"""Public examples for Advent of Code 2015, Day 6, Part 1."""

import unittest

from solution import count_lit


class LightGridExamples(unittest.TestCase):
    def test_turn_on_entire_grid(self) -> None:
        self.assertEqual(count_lit(("turn on 0,0 through 999,999",)), 1_000_000)

    def test_toggle_first_row_after_turning_on_grid(self) -> None:
        instructions = (
            "turn on 0,0 through 999,999",
            "toggle 0,0 through 999,0",
        )

        self.assertEqual(count_lit(instructions), 999_000)

    def test_turn_off_middle_four_after_turning_on_grid(self) -> None:
        instructions = (
            "turn on 0,0 through 999,999",
            "turn off 499,499 through 500,500",
        )

        self.assertEqual(count_lit(instructions), 999_996)

    def test_inclusive_ranges_and_instruction_order(self) -> None:
        instructions = (
            "turn on 0,0 through 2,2",
            "toggle 0,0 through 1,0",
            "turn off 1,1 through 2,2",
        )

        self.assertEqual(count_lit(instructions), 3)


if __name__ == "__main__":
    unittest.main()
