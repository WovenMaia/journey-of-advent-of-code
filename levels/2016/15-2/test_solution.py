"""Published examples and the Part 2 disc extension for Advent of Code 2016, Day 15."""

import unittest

from solution import first_time, parse, run


EXAMPLE = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""


class CapsuleExamples(unittest.TestCase):
    def test_published_part_one_example_still_aligns(self) -> None:
        self.assertEqual(first_time(parse(EXAMPLE)), 5)

    def test_part_two_adds_the_seventh_disc(self) -> None:
        self.assertEqual(run(EXAMPLE)["a"], 85)

    def test_invalid_input_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid disc"):
            parse("not a disc")


if __name__ == "__main__":
    unittest.main()
