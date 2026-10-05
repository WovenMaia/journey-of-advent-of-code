"""Public examples for Advent of Code 2015, Day 22, Part 1."""

import unittest

from solution import minimum_mana, parse_boss


class WizardExamples(unittest.TestCase):
    def test_poison_and_missile_example(self) -> None:
        self.assertEqual(minimum_mana("Hit Points: 13\nDamage: 8\n", player_hp=10, mana=250), 226)

    def test_recharge_and_effects_example(self) -> None:
        self.assertEqual(minimum_mana("Hit Points: 14\nDamage: 8\n", player_hp=10, mana=250), 641)

    def test_parser_reads_boss(self) -> None:
        self.assertEqual(parse_boss("Hit Points: 13\nDamage: 8\n"), (13, 8))


if __name__ == "__main__":
    unittest.main()
