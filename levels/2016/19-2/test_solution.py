"""Published examples for Advent of Code 2016, Day 19, Part 2."""

import unittest

from solution import winner


class AcrossCircleExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(winner(5), 2)

    def test_power_of_three_boundaries(self) -> None:
        self.assertEqual(winner(1), 1)
        self.assertEqual(winner(3), 3)
        self.assertEqual(winner(4), 1)
        self.assertEqual(winner(6), 3)

    def test_non_positive_counts_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "positive"):
            winner(0)


if __name__ == "__main__":
    unittest.main()
