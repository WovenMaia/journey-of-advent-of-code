"""Public examples for Advent of Code 2016, Day 8, Part 2."""

import unittest

from solution import code


EXAMPLE = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""


class DisplayExamples(unittest.TestCase):
    def test_published_example_is_rendered(self) -> None:
        self.assertEqual(code(EXAMPLE, 7, 3), ".#..#.#\n#.#....\n.#.....")

    def test_invalid_command_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid command"):
            code("spin screen")


if __name__ == "__main__":
    unittest.main()
