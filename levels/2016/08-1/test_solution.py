"""Public examples for Advent of Code 2016, Day 8, Part 1."""

import unittest

from solution import lit_pixels, render, run


EXAMPLE = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""


class DisplayExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(lit_pixels(EXAMPLE, 7, 3), 6)
        self.assertEqual(render(run(EXAMPLE, 7, 3)), ".#..#.#\n#.#....\n.#.....")

    def test_unknown_command_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid command"):
            run("spin screen")


if __name__ == "__main__":
    unittest.main()
