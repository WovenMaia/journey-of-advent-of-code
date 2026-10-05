"""Public examples for Advent of Code 2016, Day 10, Part 2."""

import unittest

from solution import output_product


EXAMPLE = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""


class BalanceBotsExamples(unittest.TestCase):
    def test_published_example_outputs(self) -> None:
        self.assertEqual(output_product(EXAMPLE), 30)

    def test_invalid_instruction_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid instruction"):
            output_product("hand chip to bot 1")


if __name__ == "__main__":
    unittest.main()
