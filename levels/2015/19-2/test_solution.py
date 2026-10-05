"""Public examples for Advent of Code 2015, Day 19, Part 2."""

import unittest

from solution import grammar_steps, part_two


RULES = """\
e => H
e => O
H => HO
H => OH
O => HH
"""


class MedicineReductionExamples(unittest.TestCase):
    def test_hoh_takes_three_steps(self) -> None:
        self.assertEqual(part_two(RULES + "\nHOH\n"), 3)

    def test_hohoho_takes_six_steps(self) -> None:
        self.assertEqual(part_two(RULES + "\nHOHOHO\n"), 6)

    def test_canonical_grammar_count(self) -> None:
        self.assertEqual(grammar_steps("CRnFYFYFAr"), 1)


if __name__ == "__main__":
    unittest.main()
