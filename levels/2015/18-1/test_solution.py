"""Public examples for Advent of Code 2015, Day 18, Part 1."""

import unittest

from solution import parse_grid, part_one, step


EXAMPLE = """\
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""


class LightExamples(unittest.TestCase):
    def test_example_after_four_steps(self) -> None:
        self.assertEqual(part_one(EXAMPLE, steps=4), 4)

    def test_single_step_matches_public_configuration(self) -> None:
        expected = ("..##..", "..##.#", "...##.", "......", "#.....", "#.##..")
        self.assertEqual(step(parse_grid(EXAMPLE)), expected)

    def test_parser_rejects_non_rectangular_grid(self) -> None:
        with self.assertRaisesRegex(ValueError, "rectangle"):
            parse_grid("#.\n###\n")


if __name__ == "__main__":
    unittest.main()
