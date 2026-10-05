"""Public examples for Advent of Code 2016, Day 11, Part 1."""

import unittest

from solution import minimum_steps


EXAMPLE = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""


class ElevatorExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(minimum_steps(EXAMPLE), 11)

    def test_unreachable_configuration_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "incomplete component pair"):
            minimum_steps("The first floor contains a hydrogen generator.")


if __name__ == "__main__":
    unittest.main()
