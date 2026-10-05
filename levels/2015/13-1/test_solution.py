"""Public examples for Advent of Code 2015, Day 13, Part 1."""

import unittest

from solution import parse_preferences, part_one, total_happiness


EXAMPLE = """\
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""


class KnightsOfTheDinnerTableExamples(unittest.TestCase):
    def test_public_example(self) -> None:
        self.assertEqual(part_one(EXAMPLE), 330)

    def test_circular_score_counts_both_directions_and_the_wraparound_pair(self) -> None:
        document = """\
Alice would gain 1 happiness units by sitting next to Bob.
Alice would gain 30 happiness units by sitting next to Carol.
Bob would gain 10 happiness units by sitting next to Alice.
Bob would gain 2 happiness units by sitting next to Carol.
Carol would gain 20 happiness units by sitting next to Bob.
Carol would gain 3 happiness units by sitting next to Alice.
"""
        preferences = parse_preferences(document)
        self.assertEqual(
            total_happiness(("Alice", "Bob", "Carol"), preferences),
            66,
        )


if __name__ == "__main__":
    unittest.main()
