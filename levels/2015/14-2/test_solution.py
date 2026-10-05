"""Public examples for Advent of Code 2015, Day 14, Part 2."""

import unittest

from solution import Reindeer, distance_after, part_two


EXAMPLE = """\
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""


class ReindeerOlympicsExamples(unittest.TestCase):
    def test_public_example_after_one_thousand_seconds(self) -> None:
        self.assertEqual(part_two(EXAMPLE, seconds=1000), 689)

    def test_points_include_every_reindeer_tied_for_the_lead(self) -> None:
        tied = """\
Alpha can fly 1 km/s for 1 seconds, but then must rest for 1 seconds.
Beta can fly 1 km/s for 1 seconds, but then must rest for 1 seconds.
"""
        self.assertEqual(part_two(tied, seconds=4), 4)

    def test_distance_helper_matches_part_one_boundaries(self) -> None:
        comet = Reindeer("Comet", speed=14, flight_seconds=10, rest_seconds=127)
        self.assertEqual(distance_after(comet, 10), 140)
        self.assertEqual(distance_after(comet, 11), 140)
        self.assertEqual(distance_after(comet, 138), 154)

    def test_empty_document_has_no_winner(self) -> None:
        self.assertEqual(part_two("", seconds=1000), 0)


if __name__ == "__main__":
    unittest.main()
