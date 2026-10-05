"""Published examples for Advent of Code 2016, Day 24, Part 2."""

import unittest

from solution import shortest_route


EXAMPLE = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########
"""


class ReturnRouteExamples(unittest.TestCase):
    def test_published_map_with_return_to_zero(self) -> None:
        self.assertEqual(shortest_route(EXAMPLE), 20)

    def test_single_target_round_trip(self) -> None:
        self.assertEqual(shortest_route("#####\n#0.1#\n#####\n"), 4)

    def test_missing_origin_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "starting"):
            shortest_route("###\n#1#\n###\n")


if __name__ == "__main__":
    unittest.main()
