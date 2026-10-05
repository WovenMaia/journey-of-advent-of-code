# 2015 Day 16, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/16).

## First idea

I reused the Part 1 parser and changed matching to apply the retroencabulator's ranges: cats and trees must be greater than the reference, pomeranians and goldfish must be fewer, and every other observed compound must equal its reference.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover strict greater-than and fewer-than boundaries, exact-value compounds, mismatches, and unknown compounds.

## Complexity

With **N** candidates and at most **K** observations per candidate, matching takes $O(NK)$ time and $O(NK)$ space for the parsed candidates.
