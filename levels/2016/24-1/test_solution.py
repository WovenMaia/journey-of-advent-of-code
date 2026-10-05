"""Published examples for Advent of Code 2016, Day 24, Part 1."""

import unittest

from solution import shortest_route


EXAMPLE = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########
"""


class RouteExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(shortest_route(EXAMPLE), 14)

    def test_single_target(self) -> None:
        self.assertEqual(shortest_route("#####\n#0.1#\n#####\n"), 2)

    def test_origin_is_required(self) -> None:
        with self.assertRaisesRegex(ValueError, "starting"):
            shortest_route("###\n#1#\n###\n")


if __name__ == "__main__":
    unittest.main()
