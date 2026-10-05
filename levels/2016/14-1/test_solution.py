"""Public examples for Advent of Code 2016, Day 14, Part 1."""

import unittest

from solution import first_triplet, hash_at, key_index


class OneTimePadExamples(unittest.TestCase):
    def test_published_first_key(self) -> None:
        self.assertEqual(key_index("abc", key_count=1), 39)

    def test_first_triplet_only(self) -> None:
        self.assertEqual(first_triplet("abcccddeee"), "c")
        self.assertIsNone(first_triplet("abcdef"))

    def test_hash_is_lowercase_hex(self) -> None:
        self.assertEqual(hash_at("abc", 18), "0034e0923cc38887a57bd7b1d4f953df")


if __name__ == "__main__":
    unittest.main()
