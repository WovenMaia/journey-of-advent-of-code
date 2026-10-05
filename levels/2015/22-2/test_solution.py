"""Public examples for Advent of Code 2015, Day 22, Part 2."""

import unittest

from solution import minimum_mana


class HardWizardExamples(unittest.TestCase):
    def test_hard_mode_rejects_the_low_health_opening(self) -> None:
        with self.assertRaises(ValueError):
            minimum_mana("Hit Points: 13\nDamage: 8\n", player_hp=10, mana=250)

    def test_real_start_has_a_winning_strategy(self) -> None:
        self.assertGreater(minimum_mana("Hit Points: 55\nDamage: 8\n"), 0)


if __name__ == "__main__":
    unittest.main()
