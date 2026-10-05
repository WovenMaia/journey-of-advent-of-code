"""Public examples for Advent of Code 2015, Day 11, Part 2."""

import unittest

from solution import has_two_different_pairs, increment, is_valid, next_password, part_two


class CorporatePolicyExamples(unittest.TestCase):
    def test_public_next_password_examples(self) -> None:
        self.assertEqual(next_password("abcdefgh"), "abcdffaa")
        self.assertEqual(next_password("ghijklmn"), "ghjaabcc")

    def test_part_two_advances_past_the_first_valid_password(self) -> None:
        self.assertEqual(part_two("abcdefgh"), "abcdffbb")
        self.assertEqual(part_two("ghijklmn"), "ghjbbcdd")

    def test_public_validity_examples(self) -> None:
        self.assertFalse(is_valid("hijklmmn"))
        self.assertFalse(is_valid("abbceffg"))
        self.assertFalse(is_valid("abbcegjk"))
        self.assertTrue(is_valid("abcdffaa"))
        self.assertTrue(is_valid("ghjaabcc"))

    def test_increment_wraps_at_the_right_edge(self) -> None:
        self.assertEqual(increment("abcdefgh"), "abcdefgi")
        self.assertEqual(increment("abcdefgh"[:-1] + "z"), "abcdefha")
        self.assertEqual(increment("zzzzzzzz"), "aaaaaaaa")

    def test_pairs_must_be_different_and_non_overlapping(self) -> None:
        self.assertFalse(has_two_different_pairs("aaaaaaaab"))
        self.assertFalse(has_two_different_pairs("aaaaaaab"))
        self.assertTrue(has_two_different_pairs("aabbcccc"))

    def test_malformed_passwords_are_rejected(self) -> None:
        self.assertFalse(is_valid("short"))
        self.assertFalse(is_valid("abcdefgh1"))
        with self.assertRaises(ValueError):
            part_two("short")


if __name__ == "__main__":
    unittest.main()
