"""Public examples for Advent of Code 2015, Day 8, Part 1."""

import unittest

from solution import memory_length, total_difference


class StringLiteralExamples(unittest.TestCase):
    def test_public_examples(self) -> None:
        literals = (r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"')

        self.assertEqual([len(literal) for literal in literals], [2, 5, 10, 6])
        self.assertEqual([memory_length(literal) for literal in literals], [0, 3, 7, 1])
        self.assertEqual(total_difference(literals), 12)

    def test_backslash_and_quote_escapes_each_use_one_memory_character(self) -> None:
        literal = r'"a\\b\"c"'

        self.assertEqual(memory_length(literal), 5)
        self.assertEqual(total_difference((literal + "\n",)), len(literal) - 5)

    def test_hexadecimal_escape_requires_two_digits(self) -> None:
        with self.assertRaises(ValueError):
            memory_length(r'"\x4"')


if __name__ == "__main__":
    unittest.main()
