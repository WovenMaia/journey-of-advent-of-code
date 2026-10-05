"""Public examples for Advent of Code 2016, Day 14, Part 2."""

import unittest

from solution import first_triplet, hash_at


class StretchedOneTimePadExamples(unittest.TestCase):
    def test_stretched_hash_example(self) -> None:
        self.assertEqual(hash_at("abc", 0), "a107ff634856bb300138cac6568c0f24")

    def test_first_triplet_still_uses_first_run(self) -> None:
        self.assertEqual(first_triplet("777abc999"), "7")
        self.assertIsNone(first_triplet("abcdef"))


if __name__ == "__main__":
    unittest.main()
