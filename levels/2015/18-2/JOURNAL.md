# 2015 Day 18, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/18).

## First idea

I reused the cellular-automaton step from Part 1, forcing the four corners on both before the first step and after every simultaneous update.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the six-by-six example's seventeen lights after five stuck-corner steps and verify that corners are restored after an update.

## Complexity

For a $W \times H$ grid and $S$ steps, the simulation takes $O(SWH)$ time and $O(WH)$ space.
