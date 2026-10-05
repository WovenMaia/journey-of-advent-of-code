"""Public examples for Advent of Code 2015, Day 8, Part 2."""

import unittest

from solution import encoded_length, total_difference


class EncodedStringExamples(unittest.TestCase):
    def test_public_examples(self) -> None:
        literals = (r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"')

        self.assertEqual([encoded_length(literal) for literal in literals], [6, 9, 16, 11])
        self.assertEqual(total_difference(literals), 19)

    def test_line_endings_are_not_encoded(self) -> None:
        literal = r'"a\\b\"c"'

        self.assertEqual(encoded_length(literal), 17)
        self.assertEqual(total_difference((literal + "\n",)), 8)

    def test_encoded_length_requires_a_quoted_literal(self) -> None:
        with self.assertRaises(ValueError):
            encoded_length("abc")


if __name__ == "__main__":
    unittest.main()
