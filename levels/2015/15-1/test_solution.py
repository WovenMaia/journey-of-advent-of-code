"""Public examples for Advent of Code 2015, Day 15, Part 1."""

import unittest

from solution import Ingredient, cookie_score, part_one


EXAMPLE = """\
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""


class ScienceForHungryPeopleExamples(unittest.TestCase):
    def test_public_example(self) -> None:
        self.assertEqual(part_one(EXAMPLE), 62842880)

    def test_negative_properties_become_zero(self) -> None:
        ingredients = (
            Ingredient("A", capacity=-1, durability=1, flavor=1, texture=1, calories=1),
        )
        self.assertEqual(cookie_score(ingredients, (10,)), 0)

    def test_empty_document_has_no_recipe(self) -> None:
        self.assertEqual(part_one(""), 0)

    def test_recipe_must_use_exactly_the_requested_teaspoons(self) -> None:
        one = "A: capacity 1, durability 1, flavor 1, texture 1, calories 1"
        self.assertEqual(part_one(one, teaspoons=10), 10_000)


if __name__ == "__main__":
    unittest.main()
