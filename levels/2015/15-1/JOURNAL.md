# 2015 Day 15, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/15).

## First idea

I parse each ingredient's five properties, enumerate every nonnegative whole-teaspoon allocation summing to 100, clip each of the four scored properties at zero, and maximize their product. Calories are parsed but excluded from Part 1's score.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the published two-ingredient example, zeroing a negative property, an empty document, and exact teaspoon allocation.

## Complexity

With **N** ingredients and **T** teaspoons, enumerating allocations takes $O(N T^{N-1})$ time and $O(T^{N-1})$ space.

The tested solution returned `13882464` for my real input. I submitted that value once for Part 1. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 15 Part 2 is next.
