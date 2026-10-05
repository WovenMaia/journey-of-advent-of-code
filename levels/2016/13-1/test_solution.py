"""Public examples for Advent of Code 2016, Day 13, Part 1."""

import unittest

from solution import is_open, run, shortest_path


class MazeExamples(unittest.TestCase):
    def test_published_route(self) -> None:
        self.assertEqual(shortest_path(10, (7, 4)), 11)

    def test_published_layout(self) -> None:
        self.assertTrue(is_open(10, 0, 0))
        self.assertFalse(is_open(10, 1, 0))
        self.assertFalse(is_open(10, -1, 0))


if __name__ == "__main__":
    unittest.main()
