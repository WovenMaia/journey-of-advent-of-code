"""Public examples and rewiring behavior for Advent of Code 2015, Day 7, Part 2."""

import unittest

from solution import evaluate_circuit, evaluate_rewired_circuit


EXAMPLE = (
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i",
)


class CircuitExamples(unittest.TestCase):
    def test_part_one_evaluator_is_reused(self) -> None:
        self.assertEqual(evaluate_circuit(EXAMPLE, "d"), 72)
        self.assertEqual(evaluate_circuit(EXAMPLE, "h"), 65_412)

    def test_part_two_overrides_b_with_part_one_signal(self) -> None:
        instructions = (
            "123 -> x",
            "NOT b -> a",
            "456 -> b",
        )

        # Part 1 gives a=65079; replacing b with 65079 makes a=456.
        self.assertEqual(evaluate_rewired_circuit(instructions), 456)

    def test_rewiring_accepts_one_shot_iterables(self) -> None:
        instructions = iter(("7 -> a", "1 -> b"))

        self.assertEqual(evaluate_rewired_circuit(instructions), 7)


if __name__ == "__main__":
    unittest.main()
