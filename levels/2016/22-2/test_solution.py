"""Published examples for Advent of Code 2016, Day 22, Part 2."""

import unittest

from solution import parse_nodes, shortest_steps


EXAMPLE = """root@ebhq-gridcenter# df -h
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     10T    8T     2T   80%
/dev/grid/node-x0-y1     11T    6T     5T   54%
/dev/grid/node-x0-y2     32T   28T     4T   87%
/dev/grid/node-x1-y0      9T    7T     2T   77%
/dev/grid/node-x1-y1      8T    0T     8T    0%
/dev/grid/node-x1-y2     11T    7T     4T   63%
/dev/grid/node-x2-y0     10T    6T     4T   60%
/dev/grid/node-x2-y1      9T    8T     1T   88%
/dev/grid/node-x2-y2      9T    6T     3T   66%
"""


class GridMovementExamples(unittest.TestCase):
    def test_published_grid_needs_seven_moves(self) -> None:
        self.assertEqual(shortest_steps(EXAMPLE), 7)

    def test_exactly_one_empty_node_is_required(self) -> None:
        text = EXAMPLE.replace(
            "node-x2-y2      9T    6T", "node-x2-y2      9T    0T"
        )
        with self.assertRaisesRegex(ValueError, "exactly one"):
            shortest_steps(text)

    def test_missing_grid_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "no grid"):
            parse_nodes("header only")


if __name__ == "__main__":
    unittest.main()
