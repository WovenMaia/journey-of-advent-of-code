"""Published examples for Advent of Code 2016, Day 18, Part 2."""

import unittest

from solution import safe_tiles


class TrapExamples(unittest.TestCase):
    def test_published_example_remains_correct_at_ten_rows(self) -> None:
        self.assertEqual(safe_tiles(".^^.^.^^^^", 10), 38)

    def test_three_row_example(self) -> None:
        self.assertEqual(safe_tiles("..^^.", 3), 6)

    def test_invalid_rows_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "row"):
            safe_tiles("..x^", 3)
        with self.assertRaisesRegex(ValueError, "positive"):
            safe_tiles(".^.", 0)


if __name__ == "__main__":
    unittest.main()
