# 2015 Day 15, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/15).

## First idea

I reused the ingredient parser, allocation enumeration, and clipped property-product score from Part 1, retaining only recipes whose calorie total is exactly 500.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the published two-ingredient example with the calorie requirement, zeroing a negative property, an empty document, exact teaspoon allocation, and rejecting recipes with the wrong calorie total.

## Complexity

With **N** ingredients and **T** teaspoons, enumerating allocations takes $O(N T^{N-1})$ time and $O(T^{N-1})$ space.

The tested solution returned `11171160` for my real input. I submitted that value once for Part 2. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 16 Part 1 is next.
