"""Public examples for Advent of Code 2015, Day 16, Part 2."""

import unittest

from solution import parse_sues, part_two


class AuntSueExamples(unittest.TestCase):
    def test_range_rules_match_strictly(self) -> None:
        document = """\
Sue 1: cats: 8, trees: 4, pomeranians: 2, goldfish: 4
Sue 2: cats: 7, trees: 3, pomeranians: 3, goldfish: 5
"""
        self.assertEqual(part_two(document), 1)

    def test_exact_rules_still_match_exactly(self) -> None:
        document = "Sue 1: children: 3, samoyeds: 2, cars: 2, perfumes: 1\n"
        self.assertEqual(part_two(document), 1)

    def test_all_observed_compounds_must_match(self) -> None:
        document = "Sue 1: cats: 8, akitas: 1\n"
        with self.assertRaisesRegex(ValueError, "found 0"):
            part_two(document)

    def test_parser_rejects_unknown_compounds(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown compound"):
            parse_sues("Sue 1: unicorns: 1\n")


if __name__ == "__main__":
    unittest.main()
