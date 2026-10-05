"""Public examples for Advent of Code 2016, Day 9, Part 1."""

import unittest

from solution import decompressed_length


class DecompressionExamples(unittest.TestCase):
    def test_published_examples(self) -> None:
        examples = {
            "ADVENT": 6,
            "A(1x5)BC": 7,
            "(3x3)XYZ": 9,
            "A(2x2)BCD(2x2)EFG": 11,
            "(6x1)(1x3)A": 6,
            "X(8x2)(3x3)ABCY": 18,
        }
        for text, expected in examples.items():
            with self.subTest(text=text):
                self.assertEqual(decompressed_length(text), expected)

    def test_whitespace_is_ignored(self) -> None:
        self.assertEqual(decompressed_length("A(1x5) B C\n"), 7)

    def test_malformed_marker_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid marker"):
            decompressed_length("A(bad)")


if __name__ == "__main__":
    unittest.main()
