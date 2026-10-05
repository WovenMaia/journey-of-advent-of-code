"""Public examples for Advent of Code 2015, Day 7, Part 1."""

import unittest

from solution import evaluate_circuit


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
    def test_example_wires(self) -> None:
        expected = {
            "d": 72,
            "e": 507,
            "f": 492,
            "g": 114,
            "h": 65_412,
            "i": 65_079,
            "x": 123,
            "y": 456,
        }

        for wire, value in expected.items():
            with self.subTest(wire=wire):
                self.assertEqual(evaluate_circuit(EXAMPLE, wire), value)

    def test_forward_references_are_resolved(self) -> None:
        instructions = (
            "a OR b -> c",
            "1 -> b",
            "2 -> a",
        )

        self.assertEqual(evaluate_circuit(instructions, "c"), 3)

    def test_signals_are_masked_to_sixteen_bits(self) -> None:
        instructions = (
            "0 -> zero",
            "NOT zero -> inverted",
            "inverted LSHIFT 1 -> shifted",
        )

        self.assertEqual(evaluate_circuit(instructions, "inverted"), 65_535)
        self.assertEqual(evaluate_circuit(instructions, "shifted"), 65_534)


if __name__ == "__main__":
    unittest.main()
