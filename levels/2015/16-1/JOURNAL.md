# 2015 Day 16, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/16).

## First idea

I parsed each candidate's observed compounds and retained the candidate whose observations all equal the known reference values. Unobserved compounds do not disqualify a candidate.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover matching observed fields, rejecting a mismatch, preserving candidate order, and malformed observations.

## Complexity

With **N** candidates and at most **K** observations per candidate, matching takes $O(NK)$ time and $O(NK)$ space for the parsed candidates.
