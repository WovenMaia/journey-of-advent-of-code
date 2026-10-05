"""Public examples for Advent of Code 2016, Day 2, Part 1."""

import unittest

from solution import code, parse_instructions


class CodeExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(code("ULL\nRRDDD\nLURDL\nUUUUD"), "1985")

    def test_invalid_moves_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid move line"):
            parse_instructions("ULL\nBAD")

    def test_empty_lines_do_not_create_digits(self) -> None:
        self.assertEqual(code("U\n\nD"), "25")


if __name__ == "__main__":
    unittest.main()
