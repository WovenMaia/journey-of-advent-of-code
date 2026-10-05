"""Public examples for Advent of Code 2016, Day 6, Part 2."""

import unittest

from solution import decode


EXAMPLE = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""


class SignalExamples(unittest.TestCase):
    def test_published_example(self) -> None:
        self.assertEqual(decode(EXAMPLE), "advent")

    def test_alphabetical_tie_break_is_stable(self) -> None:
        self.assertEqual(decode("ba\nab"), "aa")


if __name__ == "__main__":
    unittest.main()
