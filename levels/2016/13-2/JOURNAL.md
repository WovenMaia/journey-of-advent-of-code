# 2016 Day 13, Part 2

**Status:** solved (05/10/2026). The bounded-search checks pass, and the real maze was explored to 50 steps before submitting once.

## Real input and submission

There are `124` distinct locations reachable in at most 50 steps. I submitted `124` once. Advent of Code replied: “You got the second star! You are one gold star closer to fixing the sleigh.” Part 2 is solved and Day 13 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/13). In my words: count every open coordinate that the same maze walk can reach within a fixed step budget.

## Why Python

The same deque-based traversal as Part 1 makes the distance limit explicit and avoids exploring an unbounded grid.

## First idea

Keep each coordinate's shortest distance in the queue, stop expanding a node at distance 50, and count the visited set.

## Wrong turns

There were no wrong submissions. The important boundary is to count the starting location and all nodes at distance 50, while not expanding those nodes further.

## Algorithmic concept

This is **bounded breadth-first search**. The visited set is exactly the set of locations whose minimum distance is at most the limit.

## Complexity

For `v` locations reached within the limit, runtime and memory are **O(v)**. The limit makes the explored portion finite even though the maze extends indefinitely.
