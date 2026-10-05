"""Public examples for Advent of Code 2015, Day 9, Part 2."""

import unittest

from solution import longest_route, parse_distances


EXAMPLE = (
    "London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141",
)


class RouteExamples(unittest.TestCase):
    def test_public_example(self) -> None:
        self.assertEqual(longest_route(EXAMPLE), 982)

    def test_route_parser_is_undirected_and_ignores_line_endings(self) -> None:
        distances = parse_distances(
            ("A to B = 7\r\n", "B to C = 4\n", "A to C = 20")
        )

        self.assertEqual(
            distances, {("A", "B"): 7, ("B", "C"): 4, ("A", "C"): 20}
        )
        self.assertEqual(
            longest_route(iter(("A to B = 7", "B to C = 4", "A to C = 20"))),
            27,
        )

    def test_blank_lines_are_ignored(self) -> None:
        self.assertEqual(
            longest_route(("A to B = 3", "", "B to C = 5", "A to C = 20")),
            25,
        )

    def test_invalid_distance_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            parse_distances(("A -> B = 3",))


if __name__ == "__main__":
    unittest.main()
