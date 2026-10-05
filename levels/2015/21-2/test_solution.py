"""Public examples for Advent of Code 2015, Day 21, Part 2."""

import unittest

from solution import parse_boss, wins


class CombatExamples(unittest.TestCase):
    def test_public_combat_example_is_not_a_loss(self) -> None:
        self.assertTrue(wins(5, 5, (12, 7, 2)))

    def test_parser_reads_boss_stats(self) -> None:
        self.assertEqual(parse_boss("Hit Points: 12\nDamage: 7\nArmor: 2\n"), (12, 7, 2))


if __name__ == "__main__":
    unittest.main()
