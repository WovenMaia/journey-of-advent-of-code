# 2016 Day 22, Part 1

**Status:** staged (05/10/2026). The published example passes. The real input is pending because the Advent of Code session is unavailable.

## Real input and submission

No real input result is recorded yet. I did not submit an answer. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/22). In my words: count ordered pairs where nonempty data fits on another node.

## Why Python

The input is a small table of node measurements, and a direct pair count keeps the definition visible.

## First idea

Parse only node rows, then compare every source with every distinct destination. Empty sources are excluded before testing capacity.

## Wrong turns

There was no wrong algorithmic turn. The public example and an empty source check cover the pair direction and the zero case.

## Algorithmic concept

This is **compatibility counting**. A viable pair is a directed edge in a capacity relation between nodes.

## Complexity

For `n` nodes, the pair scan costs O(n squared) time and parsing uses O(n) memory.
