"""Public examples for Advent of Code 2015, Day 16, Part 1."""

import unittest

from solution import parse_sues, part_one


class AuntSueExamples(unittest.TestCase):
    def test_matching_candidate_ignores_unobserved_compounds(self) -> None:
        document = """\
Sue 1: children: 3, cars: 2
Sue 2: children: 3, cars: 9
"""
        self.assertEqual(part_one(document), 1)

    def test_all_observed_compounds_must_match(self) -> None:
        document = "Sue 1: akitas: 0, perfumes: 2\n"
        with self.assertRaisesRegex(ValueError, "found 0"):
            part_one(document)

    def test_parser_returns_candidates_in_input_order(self) -> None:
        sues = parse_sues("Sue 8: trees: 3\nSue 4: goldfish: 5\n")
        self.assertEqual([sue.number for sue in sues], [8, 4])

    def test_malformed_observation_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid observation"):
            parse_sues("Sue 1: children 3\n")


if __name__ == "__main__":
    unittest.main()
