"""Public examples for Advent of Code 2015, Day 6, Part 2."""

import unittest

from solution import total_brightness


class LightGridExamples(unittest.TestCase):
    def test_turn_on_one_light(self) -> None:
        self.assertEqual(total_brightness(("turn on 0,0 through 0,0",)), 1)

    def test_toggle_entire_grid(self) -> None:
        self.assertEqual(total_brightness(("toggle 0,0 through 999,999",)), 2_000_000)

    def test_turn_off_never_goes_below_zero(self) -> None:
        instructions = (
            "turn off 0,0 through 1,0",
            "turn on 0,0 through 0,0",
            "turn off 0,0 through 1,0",
        )

        self.assertEqual(total_brightness(instructions), 0)

    def test_inclusive_ranges_and_instruction_order(self) -> None:
        instructions = (
            "turn on 0,0 through 2,2",
            "toggle 0,0 through 1,0",
            "turn off 1,1 through 2,2",
        )

        self.assertEqual(total_brightness(instructions), 9)


if __name__ == "__main__":
    unittest.main()
