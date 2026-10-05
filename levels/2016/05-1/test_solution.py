"""Public examples for Advent of Code 2016, Day 5, Part 1."""

import unittest

from solution import password


class PasswordExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(password("abc", max_index=20_000_000), "18f47a30")

    def test_search_limit_is_explicit(self) -> None:
        with self.assertRaisesRegex(ValueError, "search exceeded"):
            password("abc", length=1, max_index=1)


if __name__ == "__main__":
    unittest.main()
