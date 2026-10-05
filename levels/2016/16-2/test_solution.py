"""Published example regression for Advent of Code 2016, Day 16, Part 2."""

import unittest

from solution import checksum, dragon_step, fill


class DragonCurveExamples(unittest.TestCase):
    def test_expansion_matches_the_published_example(self) -> None:
        self.assertEqual(dragon_step("1"), "100")

    def test_published_example_checksum(self) -> None:
        self.assertEqual(checksum(fill("10000", 20)), "01100")

    def test_invalid_data_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "bit string"):
            fill("10x", 20)


if __name__ == "__main__":
    unittest.main()
