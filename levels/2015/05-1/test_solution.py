"""Public examples for Advent of Code 2015, Day 5, Part 1."""

import unittest

from solution import count_nice_strings, is_nice


class NiceStringExamples(unittest.TestCase):
    def test_ugknbfddgicrmopn_is_nice(self) -> None:
        self.assertTrue(is_nice("ugknbfddgicrmopn"))

    def test_aaa_is_nice(self) -> None:
        self.assertTrue(is_nice("aaa"))

    def test_jchzalrnumimnmhp_is_naughty(self) -> None:
        self.assertFalse(is_nice("jchzalrnumimnmhp"))

    def test_haegwjzuvuyypxyu_is_naughty(self) -> None:
        self.assertFalse(is_nice("haegwjzuvuyypxyu"))

    def test_dvszwmarrgswjxmb_is_naughty(self) -> None:
        self.assertFalse(is_nice("dvszwmarrgswjxmb"))

    def test_example_list_contains_two_nice_strings(self) -> None:
        examples = (
            "ugknbfddgicrmopn",
            "aaa",
            "jchzalrnumimnmhp",
            "haegwjzuvuyypxyu",
            "dvszwmarrgswjxmb",
        )

        self.assertEqual(count_nice_strings(examples), 2)


if __name__ == "__main__":
    unittest.main()
