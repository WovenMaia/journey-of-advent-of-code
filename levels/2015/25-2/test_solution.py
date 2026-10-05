"""Completion record for Advent of Code 2015, Day 25, Part 2."""

import unittest

from solution import part_two


class CompletionGrant(unittest.TestCase):
    def test_part_two_is_automatically_granted(self) -> None:
        self.assertEqual(part_two(), "granted")


if __name__ == "__main__":
    unittest.main()
