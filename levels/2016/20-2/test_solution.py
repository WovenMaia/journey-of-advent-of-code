"""Published examples for Advent of Code 2016, Day 20, Part 2."""

import unittest

from solution import allowed_count


class FirewallExamples(unittest.TestCase):
    def test_published_example_counts_two_allowed_addresses(self) -> None:
        self.assertEqual(allowed_count("5-8\n0-2\n4-7\n", maximum=9), 2)

    def test_overlaps_and_fully_blocked_space(self) -> None:
        self.assertEqual(allowed_count("0-1\n3-4\n", maximum=5), 2)
        self.assertEqual(allowed_count("0-5\n", maximum=5), 0)

    def test_malformed_ranges_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "ranges"):
            allowed_count("4-x")


if __name__ == "__main__":
    unittest.main()
