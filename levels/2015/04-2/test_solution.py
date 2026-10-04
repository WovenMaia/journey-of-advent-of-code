"""Part 2 rule checks for Advent of Code 2015, Day 4."""

import unittest
from hashlib import md5

from solution import lowest_adventcoin_number_with_six_zeroes


class AdventCoinPartTwoRules(unittest.TestCase):
    def test_abcdef_lowest_suffix_has_six_zeroes(self) -> None:
        number = lowest_adventcoin_number_with_six_zeroes("abcdef")

        self.assertEqual(number, 6742839)
        self.assertTrue(md5(f"abcdef{number}".encode()).hexdigest().startswith("000000"))


if __name__ == "__main__":
    unittest.main()
