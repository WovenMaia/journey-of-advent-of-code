# 2015 Day 17, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/17).

## First idea

I kept the Part 1 include/exclude recursion, but each memoized state now returns both the smallest number of containers found and the number of ways to achieve that minimum. Equal-sized containers remain distinct because recursion is indexed by position.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the public example's three minimum-container combinations, duplicate-capacity identity, and invalid capacities.

## Complexity

With **N** containers and target **T**, memoized states take $O(NT)$ time and space; each state stores a minimum container count and its number of ways.
