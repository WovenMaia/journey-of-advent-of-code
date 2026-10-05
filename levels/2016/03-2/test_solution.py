"""Public examples for Advent of Code 2016, Day 3, Part 2."""

import unittest

from solution import count_valid, is_valid, parse_rows


class TriangleExamples(unittest.TestCase):
    def test_published_column_example(self) -> None:
        text = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603"""
        self.assertEqual(count_valid(text), 6)

    def test_column_order_changes_the_answer(self) -> None:
        self.assertEqual(count_valid("5 5 5\n10 10 5\n25 5 5"), 1)
        self.assertTrue(is_valid((5, 5, 5)))

    def test_incomplete_groups_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "grouped in threes"):
            parse_rows("3 4 5")


if __name__ == "__main__":
    unittest.main()
