"""Public examples for Advent of Code 2015, Day 5, Part 2."""

import unittest

from solution import count_nice_strings, is_nice


class NiceStringExamples(unittest.TestCase):
    def test_qjhvhtzxzqqjkmpb_is_nice(self) -> None:
        self.assertTrue(is_nice("qjhvhtzxzqqjkmpb"))

    def test_xxyxx_is_nice(self) -> None:
        self.assertTrue(is_nice("xxyxx"))

    def test_uurcxstgmygtbstg_is_naughty(self) -> None:
        self.assertFalse(is_nice("uurcxstgmygtbstg"))

    def test_ieodomkazucvgmuy_is_naughty(self) -> None:
        self.assertFalse(is_nice("ieodomkazucvgmuy"))

    def test_overlapping_pair_does_not_count(self) -> None:
        self.assertFalse(is_nice("aaa"))

    def test_example_list_contains_two_nice_strings(self) -> None:
        examples = (
            "qjhvhtzxzqqjkmpb",
            "xxyxx",
            "uurcxstgmygtbstg",
            "ieodomkazucvgmuy",
        )

        self.assertEqual(count_nice_strings(examples), 2)


if __name__ == "__main__":
    unittest.main()
