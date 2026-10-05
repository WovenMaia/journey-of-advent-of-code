"""Published examples for Advent of Code 2016, Day 20, Part 1."""

import unittest

from solution import first_allowed


class FirewallExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(first_allowed("5-8\n0-2\n4-7\n", maximum=9), 3)

    def test_overlaps_and_adjacent_ranges(self) -> None:
        self.assertEqual(first_allowed("0-1\n3-4\n", maximum=5), 2)
        self.assertEqual(first_allowed("0-5\n", maximum=5), None)

    def test_malformed_ranges_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "ranges"):
            first_allowed("4-x")


if __name__ == "__main__":
    unittest.main()
