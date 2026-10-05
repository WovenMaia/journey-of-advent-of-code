"""Public examples for Advent of Code 2016, Day 15, Part 1."""

import unittest

from solution import first_time, parse


EXAMPLE = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""


class CapsuleExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(first_time(parse(EXAMPLE)), 5)

    def test_parse_preserves_disc_order(self) -> None:
        self.assertEqual(parse(EXAMPLE)[1], (2, 2, 1))

    def test_invalid_input_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid disc"):
            parse("not a disc")


if __name__ == "__main__":
    unittest.main()
