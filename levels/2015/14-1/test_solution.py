"""Public examples for Advent of Code 2015, Day 14, Part 1."""

import unittest

from solution import Reindeer, distance_after, part_one


EXAMPLE = """\
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""


class ReindeerOlympicsExamples(unittest.TestCase):
    def test_public_example_after_one_thousand_seconds(self) -> None:
        self.assertEqual(part_one(EXAMPLE, seconds=1000), 1120)

    def test_distance_handles_partial_flight_and_rest_cycles(self) -> None:
        comet = Reindeer("Comet", speed=14, flight_seconds=10, rest_seconds=127)
        self.assertEqual(distance_after(comet, 10), 140)
        self.assertEqual(distance_after(comet, 11), 140)
        self.assertEqual(distance_after(comet, 138), 154)

    def test_empty_document_has_no_winner(self) -> None:
        self.assertEqual(part_one("", seconds=1000), 0)


if __name__ == "__main__":
    unittest.main()
