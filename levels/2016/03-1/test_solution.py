"""Public examples for Advent of Code 2016, Day 3, Part 1."""

import unittest

from solution import count_valid, is_valid, parse_triangles


class TriangleExamples(unittest.TestCase):
    def test_published_impossible_triangle(self) -> None:
        self.assertEqual(count_valid("5 10 25"), 0)

    def test_valid_triangle(self) -> None:
        self.assertTrue(is_valid((3, 4, 5)))
        self.assertEqual(count_valid("  3  4  5\n5 10 25"), 1)

    def test_triangle_inequality_is_strict(self) -> None:
        self.assertFalse(is_valid((1, 2, 3)))

    def test_malformed_rows_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid triangle row"):
            parse_triangles("3 4")


if __name__ == "__main__":
    unittest.main()
