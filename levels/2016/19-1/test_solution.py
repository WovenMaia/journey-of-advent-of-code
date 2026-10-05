"""Published examples for Advent of Code 2016, Day 19, Part 1."""

import unittest

from solution import winner


class JosephusExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(winner(5), 3)

    def test_power_of_two_and_single_elf(self) -> None:
        self.assertEqual(winner(1), 1)
        self.assertEqual(winner(8), 1)

    def test_non_positive_counts_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "positive"):
            winner(0)


if __name__ == "__main__":
    unittest.main()
