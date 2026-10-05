"""Published examples for Advent of Code 2016, Day 17, Part 2."""

import unittest

from solution import longest_path_length


class VaultExamples(unittest.TestCase):
    def test_published_longest_lengths(self) -> None:
        self.assertEqual(longest_path_length("ihgpwlah"), 370)
        self.assertEqual(longest_path_length("kglvqrro"), 492)
        self.assertEqual(longest_path_length("ulqzkmiv"), 830)

    def test_unreachable_vault_has_no_successful_path(self) -> None:
        self.assertEqual(longest_path_length("hijkl"), 0)

    def test_empty_passcode_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "passcode"):
            longest_path_length("  ")


if __name__ == "__main__":
    unittest.main()
