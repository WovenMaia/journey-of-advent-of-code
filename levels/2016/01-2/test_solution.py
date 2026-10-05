"""Public examples for Advent of Code 2016, Day 1, Part 2."""

import unittest

from solution import distance, first_revisited, parse_instructions


class RevisitedExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(distance("R8, R4, R4, R8"), 4)
        self.assertEqual(first_revisited("R8, R4, R4, R8"), (4, 0))

    def test_start_is_a_visited_location(self) -> None:
        self.assertEqual(first_revisited("R1, R1, R1, R1"), (0, 0))

    def test_route_without_revisit_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "never visits"):
            distance("R2, L3")

    def test_parser_rejects_malformed_tokens(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid instruction"):
            parse_instructions("R2, nope")


if __name__ == "__main__":
    unittest.main()
