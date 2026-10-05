"""Public examples for Advent of Code 2015, Day 12, Part 1."""

import unittest

from solution import part_one, sum_numbers


class JsAbacusFrameworkExamples(unittest.TestCase):
    def test_public_examples(self) -> None:
        self.assertEqual(part_one("[1,2,3]"), 6)
        self.assertEqual(part_one('{"a":2,"b":4}'), 6)
        self.assertEqual(part_one("[[[3]]]"), 3)
        self.assertEqual(part_one('{"a":{"b":4},"c":-1}'), 3)
        self.assertEqual(part_one('{"a":[-1,1]}'), 0)
        self.assertEqual(part_one('[-1,{"a":1}]'), 0)
        self.assertEqual(part_one("[]"), 0)
        self.assertEqual(part_one("{}"), 0)

    def test_numbers_inside_strings_are_not_counted(self) -> None:
        self.assertEqual(part_one('{"a":"123", "b":[4, "-5"]}'), 4)

    def test_decoded_values_can_be_summed_directly(self) -> None:
        self.assertEqual(sum_numbers([1, {"nested": [-2, 3]}, "ignored"]), 2)


if __name__ == "__main__":
    unittest.main()
