"""Public examples for Advent of Code 2015, Day 15, Part 2."""

import unittest

from solution import Ingredient, cookie_score, part_two


EXAMPLE = """\
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""


class ScienceForHungryPeopleExamples(unittest.TestCase):
    def test_public_example_with_500_calories(self) -> None:
        self.assertEqual(part_two(EXAMPLE), 57_600_000)

    def test_negative_properties_become_zero(self) -> None:
        ingredients = (
            Ingredient("A", capacity=-1, durability=1, flavor=1, texture=1, calories=1),
        )
        self.assertEqual(cookie_score(ingredients, (10,)), 0)

    def test_empty_document_has_no_recipe(self) -> None:
        self.assertEqual(part_two(""), 0)

    def test_recipe_must_use_exactly_the_requested_teaspoons(self) -> None:
        one = "A: capacity 1, durability 1, flavor 1, texture 1, calories 10"
        self.assertEqual(part_two(one, teaspoons=10, calories=100), 10_000)

    def test_recipes_without_requested_calories_are_rejected(self) -> None:
        one = "A: capacity 1, durability 1, flavor 1, texture 1, calories 1"
        self.assertEqual(part_two(one, teaspoons=10, calories=500), 0)


if __name__ == "__main__":
    unittest.main()
