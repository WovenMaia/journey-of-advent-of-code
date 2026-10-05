"""Published examples for Advent of Code 2016, Day 18, Part 1."""

import unittest

from solution import safe_tiles


class TrapExamples(unittest.TestCase):
    def test_small_published_example(self) -> None:
        self.assertEqual(safe_tiles("..^^.", 3), 6)

    def test_ten_row_published_example(self) -> None:
        self.assertEqual(safe_tiles(".^^.^.^^^^", 10), 38)

    def test_invalid_rows_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "row"):
            safe_tiles("..x^", 3)
        with self.assertRaisesRegex(ValueError, "positive"):
            safe_tiles(".^.", 0)


if __name__ == "__main__":
    unittest.main()
