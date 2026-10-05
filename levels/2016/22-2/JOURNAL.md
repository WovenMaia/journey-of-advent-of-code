# 2016 Day 22, Part 2

**Status:** staged (05/10/2026). The published example passes. The real input is pending because the Advent of Code session is unavailable.

## Real input and submission

No real input result is recorded yet. I did not submit an answer. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/22). In my words: move the goal data to the origin through adjacent storage nodes.

## Why Python

The node layout becomes a small state graph once oversized nodes are treated as walls. Breadth first search then gives the shortest sequence of empty node and goal positions.

## First idea

Find the sole empty node, identify the rightmost top row node as the goal, and search states `(empty, goal)`. A move swaps the empty node with a normal neighbor or moves the goal data when the goal is adjacent.

## Wrong turns

There was no wrong algorithmic turn. The example and two empty node validation checks cover the state representation assumptions.

## Algorithmic concept

This is **state space search with a sliding vacancy**. The empty node is the movable tool, and the goal data is a second tracked token.

## Complexity

For `n` open cells, breadth first search uses O(n squared) possible pair states and O(n squared) memory in the worst case.
