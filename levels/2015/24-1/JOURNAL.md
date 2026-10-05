# 2015 Day 24, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/24).

## First idea

I enumerated first-group subsets by increasing package count, ordered each size by quantum entanglement, and recursively verified that the remainder can split into two equal groups.

## Wrong turns

There were no wrong turns.

## Public examples

The ten-package example selects `11 9` with quantum entanglement 99.

## Complexity

Subset generation is exponential in package count, but the smallest-group-first ordering and memoized remainder checks prune the real search.
