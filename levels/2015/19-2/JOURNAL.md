# 2015 Day 19, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/19).

## First idea

The real input follows the puzzle's nested grammar. Token counting gives the exact reduction length: total tokens minus `Rn`, `Ar`, twice `Y`, and the final `e` seed. The small examples are checked by reversing replacements to `e`.

## Wrong turns

A forward molecule search would explode, so I kept it out of the real-input path.

## Public examples

The tests cover the three-step HOH and six-step HOHOHO examples and the grammar identity.

## Complexity

The grammar count is $O(N)$ in molecule token count and $O(1)$ auxiliary space; the tiny example reducer is memoized for its bounded input.
