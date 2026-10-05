"""Public examples for Advent of Code 2015, Day 24, Part 2."""

import unittest

from solution import parse_weights, part_two


EXAMPLE = """\
1
2
3
4
5
7
8
9
10
11
"""


class SleighExamples(unittest.TestCase):
    def test_four_groups_choose_two_package_first_group(self) -> None:
        self.assertEqual(part_two(EXAMPLE), 44)

    def test_parser_rejects_non_positive_weight(self) -> None:
        with self.assertRaises(ValueError):
            parse_weights("1\n-2\n")


if __name__ == "__main__":
    unittest.main()
