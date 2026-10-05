# 2015 Day 17, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/17).

## First idea

I count include/exclude choices recursively, memoized by the next container and the remaining volume. Indexing containers rather than capacities keeps equal-sized containers distinct, as required by the public example.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the public four-combination example, duplicate-capacity identity, and invalid capacities.

## Complexity

With **N** containers and target **T**, memoized counting takes $O(NT)$ time and $O(NT)$ space.
