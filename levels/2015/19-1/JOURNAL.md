# 2015 Day 19, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/19).

## First idea

I applied every replacement at every occurrence and collected the resulting molecules in a set, so duplicate outcomes collapse naturally.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the HOH and HOHOHO examples, including duplicate one-step outcomes.

## Complexity

For molecule length $N$ and replacement count $R$, the scan takes $O(RN)$ time and stores at most $O(RN)$ generated text.
