# 2015 Day 18, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/18).

## First idea

I represented the grid as immutable rows and built each next grid from the previous one, counting the eight in-bounds neighbours for every light so updates remain simultaneous.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the six-by-six example after one and four steps, plus malformed-row rejection.

## Complexity

For a $W \times H$ grid and $S$ steps, the simulation takes $O(SWH)$ time and $O(WH)$ space.
