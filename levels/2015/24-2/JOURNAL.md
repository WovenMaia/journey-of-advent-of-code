# 2015 Day 24, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/24).

## First idea

I used the same verified remainder partitioning with four target groups, still minimizing first-group size before quantum entanglement.

## Wrong turns

There were no wrong turns.

## Public examples

The ten-package example selects the two-package group with quantum entanglement 44.

## Complexity

The search remains exponential in package count, with memoized remainder states and a mandatory lowest-index package in each later group to remove symmetry.
