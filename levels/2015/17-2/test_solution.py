"""Public examples for Advent of Code 2015, Day 17, Part 2."""

import unittest

from solution import parse_containers, part_two


class ContainerExamples(unittest.TestCase):
    def test_public_example_counts_minimum_container_combinations(self) -> None:
        document = """\
20
15
10
5
5
"""
        self.assertEqual(part_two(document, target=25), 3)

    def test_duplicate_capacities_are_distinct_minimum_containers(self) -> None:
        self.assertEqual(part_two("5\n5\n", target=5), 2)

    def test_parser_rejects_non_positive_capacity(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be positive"):
            parse_containers("0\n")


if __name__ == "__main__":
    unittest.main()
