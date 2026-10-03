"""Public examples for Advent of Code 2015, Day 2, Part 2."""

import unittest

from solution import ribbon_for_present, total_ribbon


class RibbonExamples(unittest.TestCase):
    def test_regular_box(self) -> None:
        self.assertEqual(ribbon_for_present("2x3x4"), 34)

    def test_box_with_repeated_shortest_side(self) -> None:
        self.assertEqual(ribbon_for_present("1x1x10"), 14)

    def test_multiple_presents(self) -> None:
        self.assertEqual(total_ribbon("2x3x4\n1x1x10\n"), 48)

    def test_rejects_malformed_dimensions(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid dimensions"):
            ribbon_for_present("2x3")

    def test_rejects_non_positive_dimensions(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be positive"):
            ribbon_for_present("2x0x4")


if __name__ == "__main__":
    unittest.main()
