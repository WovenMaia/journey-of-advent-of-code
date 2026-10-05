# 2015 Day 25, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/25).

## First idea

The diagonal position is a triangular-number index, so modular exponentiation jumps directly to the requested code without generating the preceding grid.

## Wrong turns

There were no wrong turns.

## Public examples

The tests verify the first diagonal and the published 6-by-6 corner code.

## Complexity

The answer uses $O(\log N)$ modular multiplication for position $N$ and constant space.
