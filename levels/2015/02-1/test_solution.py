"""Public examples for Advent of Code 2015, Day 2, Part 1."""

import unittest

from solution import paper_for_present, total_paper


class WrappingPaperExamples(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(paper_for_present("2x3x4"), 58)
        self.assertEqual(paper_for_present("1x1x10"), 43)

    def test_total_for_multiple_presents(self) -> None:
        self.assertEqual(total_paper("2x3x4\n1x1x10\n"), 101)

    def test_rejects_non_positive_dimensions(self) -> None:
        with self.assertRaisesRegex(ValueError, "positive"):
            paper_for_present("2x0x4")

    def test_rejects_malformed_dimensions(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid dimensions"):
            paper_for_present("2x3")


if __name__ == "__main__":
    unittest.main()
