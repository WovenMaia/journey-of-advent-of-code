# 2015 Day 23, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/23).

## First idea

I parsed the six instructions into small immutable records and ran a two-register instruction pointer until it left the program.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the published `jio` example and an even-register conditional jump.

## Complexity

Execution uses $O(1)$ register state and $O(P)$ time for $P$ executed instructions.
