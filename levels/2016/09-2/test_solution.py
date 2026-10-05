"""Public examples for Advent of Code 2016, Day 9, Part 2."""

import unittest

from solution import decompressed_length


class RecursiveDecompressionExamples(unittest.TestCase):
    def test_published_examples(self) -> None:
        examples = {
            "ADVENT": 6,
            "(3x3)XYZ": 9,
            "X(8x2)(3x3)ABCY": 20,
            "(27x12)(20x12)(13x14)(7x10)(1x12)A": 241920,
            "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN": 445,
        }
        for text, expected in examples.items():
            with self.subTest(text=text):
                self.assertEqual(decompressed_length(text), expected)

    def test_malformed_marker_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid marker"):
            decompressed_length("A(bad)")


if __name__ == "__main__":
    unittest.main()
