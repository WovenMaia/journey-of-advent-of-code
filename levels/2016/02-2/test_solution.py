"""Public examples for Advent of Code 2016, Day 2, Part 2."""

import unittest

from solution import code, parse_instructions


class CodeExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(code("ULL\nRRDDD\nLURDL\nUUUUD"), "5DB3")

    def test_edges_are_ignored(self) -> None:
        self.assertEqual(code("U\nL\nD\nR"), "5556")

    def test_invalid_moves_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid move line"):
            parse_instructions("ULL\nBAD")


if __name__ == "__main__":
    unittest.main()
