# 2016 Day 13, Part 1

**Status:** solved (05/10/2026). The published favorite-number example passes, and breadth-first search finished on my real input before submitting once.

## Real input and submission

The shortest route from `(1,1)` to `(31,39)` is `92` steps. I submitted `92` once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 1 is solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/13). In my words: compute the infinite grid from a favorite number, then find the shortest walk through open cells.

## Why Python

Python's deque makes the breadth-first frontier explicit while keeping the coordinate and wall rules easy to inspect.

## First idea

Treat each coordinate as a graph node, generate its four non-negative neighbors, and stop BFS when the target is dequeued.

## Wrong turns

There were no wrong submissions. I briefly checked the public favorite number rather than the real input while shaping the example test; the test now keeps the example target explicit.

## Algorithmic concept

This is **breadth-first search** on an implicit unweighted graph. The first visit to a coordinate is its shortest distance because every move costs one step.

## Complexity

For `v` coordinates reached before the target, runtime and memory are **O(v)**. The grid itself is implicit; only the frontier and visited coordinates are stored.
