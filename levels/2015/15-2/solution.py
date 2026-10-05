"""Solution for Advent of Code 2015, Day 15, Part 2."""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Ingredient:
    """An ingredient's properties per teaspoon."""

    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


_LINE = re.compile(
    r"^(\w+): capacity (-?\d+), durability (-?\d+), "
    r"flavor (-?\d+), texture (-?\d+), calories (-?\d+)$"
)


def parse_ingredients(document: str) -> tuple[Ingredient, ...]:
    """Parse ingredient descriptions from the puzzle input."""
    ingredients: list[Ingredient] = []
    for line in document.splitlines():
        if not line:
            continue
        match = _LINE.fullmatch(line)
        if match is None:
            raise ValueError(f"invalid ingredient description: {line!r}")
        name, capacity, durability, flavor, texture, calories = match.groups()
        ingredients.append(
            Ingredient(
                name,
                int(capacity),
                int(durability),
                int(flavor),
                int(texture),
                int(calories),
            )
        )
    return tuple(ingredients)


def cookie_score(ingredients: tuple[Ingredient, ...], amounts: tuple[int, ...]) -> int:
    """Return a recipe's score after clipping negative properties to zero."""
    if len(ingredients) != len(amounts):
        raise ValueError("ingredients and amounts must have the same length")
    if any(amount < 0 for amount in amounts):
        raise ValueError("ingredient amounts must not be negative")
    properties = (
        sum(ingredient.capacity * amount for ingredient, amount in zip(ingredients, amounts)),
        sum(ingredient.durability * amount for ingredient, amount in zip(ingredients, amounts)),
        sum(ingredient.flavor * amount for ingredient, amount in zip(ingredients, amounts)),
        sum(ingredient.texture * amount for ingredient, amount in zip(ingredients, amounts)),
    )
    score = 1
    for property_total in properties:
        score *= max(0, property_total)
    return score


def _allocations(ingredient_count: int, teaspoons: int) -> tuple[tuple[int, ...], ...]:
    """Return every nonnegative allocation summing to ``teaspoons``."""
    if ingredient_count == 0:
        return ((),) if teaspoons == 0 else ()
    if ingredient_count == 1:
        return ((teaspoons,),)
    return tuple(
        (amount, *rest)
        for amount in range(teaspoons + 1)
        for rest in _allocations(ingredient_count - 1, teaspoons - amount)
    )


def part_two(document: str, teaspoons: int = 100, calories: int = 500) -> int:
    """Return the best score among recipes with the requested calorie total."""
    if teaspoons < 0:
        raise ValueError("teaspoons must not be negative")
    ingredients = parse_ingredients(document)
    return max(
        (
            cookie_score(ingredients, amounts)
            for amounts in _allocations(len(ingredients), teaspoons)
            if sum(ingredient.calories * amount for ingredient, amount in zip(ingredients, amounts))
            == calories
        ),
        default=0,
    )


if __name__ == "__main__":
    with open("inputs/2015/15.txt", encoding="utf-8") as input_file:
        print(part_two(input_file.read()))
