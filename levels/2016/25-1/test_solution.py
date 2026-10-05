"""Published examples for Advent of Code 2016, Day 25, Part 1."""

import unittest

from solution import lowest_clock_seed, signal


class ClockExamples(unittest.TestCase):
    def test_alternating_program_accepts_lowest_positive_seed(self) -> None:
        program = """cpy 0 b
out b
inc b
out b
jnz 1 -4
"""
        self.assertEqual(lowest_clock_seed(program, output_count=8), 1)

    def test_repeated_or_out_of_range_values_fail(self) -> None:
        self.assertEqual(signal("out 1\nout 1\n", 1, output_count=2), [1])
        self.assertEqual(signal("out 2\n", 1, output_count=1), [])

    def test_seed_can_be_used_by_out(self) -> None:
        self.assertEqual(signal("out a\n", 2, output_count=1), [])


if __name__ == "__main__":
    unittest.main()
