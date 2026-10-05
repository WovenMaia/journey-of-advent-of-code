"""Public examples for Advent of Code 2015, Day 18, Part 2."""

import unittest

from solution import parse_grid, part_two, step


EXAMPLE = """\
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""


class StuckCornerExamples(unittest.TestCase):
    def test_example_after_five_steps(self) -> None:
        self.assertEqual(part_two(EXAMPLE, steps=5), 17)
    def test_corners_are_on_before_and_after_each_step(self) -> None:
        grid = parse_grid("...\n...\n...")
        self.assertEqual(step(grid), ("#.#", "...", "#.#"))

    def test_parser_rejects_non_rectangular_grid(self) -> None:
        with self.assertRaisesRegex(ValueError, "rectangle"):
            parse_grid("#.\n###\n")


if __name__ == "__main__":
    unittest.main()
