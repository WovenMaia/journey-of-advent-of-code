"""Public examples for Advent of Code 2015, Day 12, Part 2."""

import unittest

from solution import part_two, sum_non_red


class JsAbacusFrameworkExamples(unittest.TestCase):
    def test_public_examples(self) -> None:
        self.assertEqual(part_two("[1,2,3]"), 6)
        self.assertEqual(part_two('[1,{"c":"red","b":2},3]'), 4)
        self.assertEqual(part_two('{"d":"red","e":[1,2,3,4],"f":5}'), 0)
        self.assertEqual(part_two('[1,"red",5]'), 6)

    def test_red_objects_are_excluded_recursively_but_arrays_are_not(self) -> None:
        self.assertEqual(
            part_two('[{"keep":4,"nested":{"color":"red","drop":9}}, {"keep":6}]'),
            10,
        )
        self.assertEqual(sum_non_red([1, "red", {"value": 2}]), 3)

    def test_red_property_values_are_checked_not_property_names(self) -> None:
        self.assertEqual(part_two('{"red":4,"blue":5}'), 9)


if __name__ == "__main__":
    unittest.main()
