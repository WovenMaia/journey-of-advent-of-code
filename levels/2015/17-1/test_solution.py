"""Public examples for Advent of Code 2015, Day 17, Part 1."""

import unittest

from solution import parse_containers, part_one


class ContainerExamples(unittest.TestCase):
    def test_public_example_counts_four_combinations(self) -> None:
        document = """\
20
15
10
5
5
"""
        self.assertEqual(part_one(document, target=25), 4)

    def test_duplicate_capacities_are_distinct_containers(self) -> None:
        self.assertEqual(part_one("5\n5\n", target=5), 2)

    def test_parser_rejects_non_positive_capacity(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be positive"):
            parse_containers("0\n")


if __name__ == "__main__":
    unittest.main()
