"""Public examples for Advent of Code 2016, Day 13, Part 2."""

import unittest

from solution import is_open, reachable


class MazeReachabilityExamples(unittest.TestCase):
    def test_start_is_reachable(self) -> None:
        self.assertIn((1, 1), reachable(10, 0))

    def test_walls_are_never_reachable(self) -> None:
        spaces = reachable(10, 50)
        self.assertNotIn((1, 0), spaces)
        self.assertFalse(is_open(10, 1, 0))

    def test_short_limit_keeps_frontier_bounded(self) -> None:
        self.assertEqual(len(reachable(10, 1)), 3)


if __name__ == "__main__":
    unittest.main()
