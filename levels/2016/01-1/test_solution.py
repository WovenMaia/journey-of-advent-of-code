"""Public examples for Advent of Code 2016, Day 1, Part 1."""

import unittest

from solution import destination, distance, parse_instructions


class DestinationExamples(unittest.TestCase):
    def test_published_examples(self) -> None:
        self.assertEqual(distance("R2, L3"), 5)
        self.assertEqual(distance("R2, R2, R2"), 2)
        self.assertEqual(distance("R5, L5, R5, R3"), 12)

    def test_destination_preserves_signed_coordinates(self) -> None:
        self.assertEqual(destination("L2, L2"), (-2, -2))

    def test_parser_rejects_malformed_tokens(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid instruction"):
            parse_instructions("R2, nope")


if __name__ == "__main__":
    unittest.main()
