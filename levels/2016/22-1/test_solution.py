"""Published examples for Advent of Code 2016, Day 22, Part 1."""

import unittest

from solution import parse_nodes, viable_pairs


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


class ViablePairExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(viable_pairs(EXAMPLE), 7)

    def test_empty_nodes_cannot_be_sources(self) -> None:
        text = "/dev/grid/node-x0-y0 10T 0T 10T 0%\n/dev/grid/node-x1-y0 10T 3T 7T 30%\n"
        self.assertEqual(viable_pairs(text), 1)

    def test_missing_nodes_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "no grid"):
            parse_nodes("header only")


if __name__ == "__main__":
    unittest.main()
