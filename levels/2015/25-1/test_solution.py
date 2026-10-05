"""Public examples for Advent of Code 2015, Day 25, Part 1."""

import unittest

from solution import code_at, parse_target


class CodeGridExamples(unittest.TestCase):
    def test_first_diagonal_codes(self) -> None:
        self.assertEqual(code_at(1, 1), 20151125)
        self.assertEqual(code_at(2, 1), 31916031)
        self.assertEqual(code_at(1, 2), 18749137)
        self.assertEqual(code_at(6, 6), 27995004)

    def test_parser_reads_console_message(self) -> None:
        self.assertEqual(parse_target("Enter the code at row 2978, column 3083."), (2978, 3083))


if __name__ == "__main__":
    unittest.main()
