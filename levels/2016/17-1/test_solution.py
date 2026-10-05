"""Published examples for Advent of Code 2016, Day 17, Part 1."""

import unittest

from solution import shortest_path


class VaultExamples(unittest.TestCase):
    def test_published_shortest_paths(self) -> None:
        self.assertEqual(shortest_path("ihgpwlah"), "DDRRRD")
        self.assertEqual(shortest_path("kglvqrro"), "DDUDRLRRUDRD")
        self.assertEqual(shortest_path("ulqzkmiv"), "DRURDRUDDLLDLUURRDULRLDUUDDDRR")

    def test_unreachable_vault(self) -> None:
        self.assertIsNone(shortest_path("hijkl"))

    def test_empty_passcode_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "passcode"):
            shortest_path("  ")


if __name__ == "__main__":
    unittest.main()
