"""Public examples for Advent of Code 2015, Day 19, Part 1."""

import unittest

from solution import parse, part_one


class MedicineExamples(unittest.TestCase):
    def test_hoh_has_four_distinct_one_step_molecules(self) -> None:
        document = """\
H => HO
H => OH
O => HH

HOH
"""
        self.assertEqual(part_one(document), 4)

    def test_hohoho_has_seven_distinct_one_step_molecules(self) -> None:
        document = """\
H => HO
H => OH
O => HH

HOHOHO
"""
        self.assertEqual(part_one(document), 7)

    def test_parser_requires_one_molecule(self) -> None:
        with self.assertRaises(ValueError):
            parse("H => HO\n")


if __name__ == "__main__":
    unittest.main()
