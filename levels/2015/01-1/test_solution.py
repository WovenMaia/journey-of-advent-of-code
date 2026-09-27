"""Public examples for Advent of Code 2015, Day 1, Part 1."""

import unittest

from solution import final_floor, floor_trace


class FinalFloorExamples(unittest.TestCase):
    def test_examples_that_end_at_floor_zero(self) -> None:
        for instructions in ("(())", "()()"):
            with self.subTest(instructions=instructions):
                self.assertEqual(final_floor(instructions), 0)

    def test_examples_that_end_above_ground(self) -> None:
        examples = {
            "(((": 3,
            "(()(()(": 3,
            "))(((((": 3,
        }
        for instructions, expected in examples.items():
            with self.subTest(instructions=instructions):
                self.assertEqual(final_floor(instructions), expected)

    def test_examples_that_end_below_ground(self) -> None:
        examples = {
            "())": -1,
            "))(": -1,
            ")))": -3,
            ")())())": -3,
        }
        for instructions, expected in examples.items():
            with self.subTest(instructions=instructions):
                self.assertEqual(final_floor(instructions), expected)

    def test_trace_is_a_running_sum(self) -> None:
        self.assertEqual(list(floor_trace("(()")), [0, 1, 2, 1])

    def test_rejects_non_instruction_characters(self) -> None:
        with self.assertRaisesRegex(ValueError, "position 2"):
            final_floor("(x)")


if __name__ == "__main__":
    unittest.main()
