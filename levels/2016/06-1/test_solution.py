"""Public examples for Advent of Code 2016, Day 6, Part 1."""

import unittest

from solution import decode, messages


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
        self.assertEqual(decode(EXAMPLE), "easter")

    def test_malformed_rows_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "rectangle"):
            messages("abc\nde")


if __name__ == "__main__":
    unittest.main()
